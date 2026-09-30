import json
import tempfile
import unittest
from pathlib import Path

from scripts.evaluate import build_command, load_cases, score_decision
from scripts.evaluate_tasks import grade_workspace


class EvaluationTests(unittest.TestCase):
    def test_builds_read_only_ephemeral_commands(self):
        codex = build_command("codex", Path("/tmp/work"), Path("/tmp/schema.json"))
        claude = build_command("claude", Path("/tmp/work"), Path("/tmp/schema.json"))
        self.assertIn("read-only", codex)
        self.assertIn("--ephemeral", codex)
        self.assertIn("plan", claude)
        self.assertIn("--no-session-persistence", claude)

    def test_scores_structured_routing_decision(self):
        case = {
            "id": "logging-implicit",
            "expected_action": "plan",
            "expected_skills": ["logging-observability"],
            "forbidden_skills": ["database-migration"],
        }
        result = score_decision(
            case,
            {"action": "plan", "skills": ["logging-observability"], "reason": "needed"},
        )
        self.assertTrue(result["passed"])

    def test_rejects_duplicate_case_ids_across_suites(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "one.json").write_text(json.dumps([{"id": "same"}]))
            (root / "two.json").write_text(json.dumps([{"id": "same"}]))
            with self.assertRaises(ValueError):
                load_cases(root)

    def test_grades_resulting_workspace_state_and_scope(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory)
            config = workspace / "logging.json"
            config.write_text(json.dumps({"retention_days": 30, "max_file_size_mib": 100}))
            task = {
                "allowed_changes": ["logging.json"],
                "checks": [
                    {
                        "type": "json_value",
                        "path": "logging.json",
                        "pointer": ["retention_days"],
                        "equals": 30,
                    },
                    {
                        "type": "json_value",
                        "path": "logging.json",
                        "pointer": ["max_file_size_mib"],
                        "equals": 100,
                    },
                ],
            }
            result = grade_workspace(task, workspace, {"logging.json": "old"})
            self.assertTrue(result["passed"], result)


if __name__ == "__main__":
    unittest.main()
