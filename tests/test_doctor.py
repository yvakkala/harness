import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.doctor import Doctor, parse_version
from scripts.install import Installer


class DoctorTests(unittest.TestCase):
    def test_parse_version(self):
        self.assertEqual(parse_version("2.1.277 (Claude Code)"), (2, 1, 277))
        self.assertEqual(parse_version("codex-cli 0.159.0"), (0, 159, 0))

    def test_reports_old_claude_and_missing_both_mode(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            Installer(Path(__file__).resolve().parents[1], home).install("all")
            (home / ".claude/settings.json").write_text("{}\n")
            versions = {"codex": "codex-cli 0.159.0", "claude": "2.1.181 (Claude Code)"}
            with patch.object(Doctor, "runtime_version", side_effect=lambda name: versions[name]):
                findings = Doctor(Path(__file__).resolve().parents[1], home).run()
            codes = {finding.code for finding in findings if not finding.ok}
            self.assertIn("claude-version", codes)
            self.assertIn("claude-instruction-mode", codes)

    def test_accepts_supported_claude_configuration(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            Installer(Path(__file__).resolve().parents[1], home).install("all")
            settings = {
                "pluginConfigs": {
                    "agents-md@builtin": {
                        "options": {"instructionFiles": "claude-md-and-agents-md"}
                    }
                }
            }
            (home / ".claude/settings.json").write_text(json.dumps(settings))
            versions = {"codex": "codex-cli 0.159.0", "claude": "2.1.277 (Claude Code)"}
            with patch.object(Doctor, "runtime_version", side_effect=lambda name: versions[name]):
                findings = Doctor(Path(__file__).resolve().parents[1], home).run()
            self.assertTrue(all(finding.ok for finding in findings), findings)


if __name__ == "__main__":
    unittest.main()
