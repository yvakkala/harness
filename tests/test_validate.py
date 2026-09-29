import tempfile
import unittest
import json
from pathlib import Path

from scripts.validate import validate_repository


class ValidatorTests(unittest.TestCase):
    def make_repo(self, agents_lines=10, todo=False):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        (root / "AGENTS.md").write_text("line\n" * agents_lines)
        skill = root / ".agents/skills/example"
        skill.mkdir(parents=True)
        body = "TODO\n" if todo else "Use the available tools to complete the example.\n"
        (skill / "SKILL.md").write_text(
            "---\nname: example\ndescription: Handle example tasks when explicitly requested.\n---\n\n" + body
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
            evals.mkdir()
            (evals / "cases.json").write_text(json.dumps([{"id": "missing-fields"}]))
            errors = validate_repository(root)
            self.assertTrue(any("evaluation case" in error for error in errors))
        finally:
            temp.cleanup()


if __name__ == "__main__":
    unittest.main()
