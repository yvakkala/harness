import tempfile
import unittest
import json
import hashlib
from pathlib import Path

from scripts.validate import validate_repository


class ValidatorTests(unittest.TestCase):
    def make_repo(self, agents_lines=10, todo=False):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        (root / "AGENTS.md").write_text("line\n" * agents_lines)
        (root / "VERSION").write_text("0.1.0\n")
        (root / "CHANGELOG.md").write_text("# Changelog\n")
        skill = root / ".agents/skills/example"
        skill.mkdir(parents=True)
        body = "TODO\n" if todo else "Use the available tools to complete the example.\n"
        (skill / "SKILL.md").write_text(
            "---\nname: example\ndescription: Handle example tasks when explicitly requested.\n---\n\n" + body
        )
        (skill / "agents").mkdir()
        (skill / "agents/openai.yaml").write_text(
            'interface:\n  display_name: "Example"\n  short_description: "Handle examples"\n'
        )
        evals = root / "evals"
        evals.mkdir()
        (evals / "cases.json").write_text(
            json.dumps(
                [
                    {
                        "id": "behavior",
                        "prompt": "Do the thing",
                        "expected_skills": [],
                        "expected": ["Do it"],
                        "forbidden": ["Skip it"],
                    }
                ]
            )
        )
        (evals / "routing.json").write_text(
            json.dumps(
                [
                    {
                        "id": "routing",
                        "prompt": "Route the thing",
                        "expected_action": "implement",
                        "expected_skills": [],
                        "forbidden_skills": ["example"],
                    }
                ]
            )
        )
        fixture = evals / "fixtures/example"
        fixture.mkdir(parents=True)
        (fixture / "input.json").write_text("{}\n")
        (evals / "tasks.json").write_text(
            json.dumps(
                [
                    {
                        "id": "task",
                        "fixture": "example",
                        "prompt": "Change the fixture",
                        "allowed_changes": ["input.json"],
                        "checks": [
                            {"type": "json_value", "path": "input.json", "pointer": [], "equals": {}}
                        ],
                    }
                ]
            )
        )
        digest = hashlib.sha256((skill / "SKILL.md").read_bytes()).hexdigest()
        yaml_digest = hashlib.sha256((skill / "agents/openai.yaml").read_bytes()).hexdigest()
        (root / "skills.lock.json").write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "skills": {
                        "example": {
                            "source": "local",
                            "revision": None,
                            "license": "unlicensed",
                            "files": {"SKILL.md": digest, "agents/openai.yaml": yaml_digest},
                        }
                    },
                }
            )
        )
        return temp, root

    def test_accepts_compact_valid_repository(self):
        temp, root = self.make_repo()
        try:
            self.assertEqual(validate_repository(root), [])
        finally:
            temp.cleanup()

    def test_rejects_oversized_agents_file_and_unfinished_skill(self):
        temp, root = self.make_repo(agents_lines=201, todo=True)
        try:
            errors = validate_repository(root)
            self.assertTrue(any("AGENTS.md" in error and "200" in error for error in errors))
            self.assertTrue(any("unfinished" in error for error in errors))
        finally:
            temp.cleanup()

    def test_rejects_incomplete_evaluation_case(self):
        temp, root = self.make_repo()
        try:
            evals = root / "evals"
            (evals / "cases.json").write_text(json.dumps([{"id": "missing-fields"}]))
            errors = validate_repository(root)
            self.assertTrue(any("evaluation case" in error for error in errors))
        finally:
            temp.cleanup()

    def test_rejects_tampered_skill_manifest(self):
        temp, root = self.make_repo()
        try:
            (root / ".agents/skills/example/SKILL.md").write_text("changed\n")
            errors = validate_repository(root)
            self.assertTrue(any("manifest" in error for error in errors))
        finally:
            temp.cleanup()


if __name__ == "__main__":
    unittest.main()
