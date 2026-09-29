import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from scripts.install import Installer, InstallConflict


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.source = Path(__file__).resolve().parents[1]
        self.temp = tempfile.TemporaryDirectory()
        self.home = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def test_installs_managed_copies_for_both_runtimes(self):
        Installer(self.source, self.home).install("all")

        for runtime in (".codex", ".claude"):
            agents = self.home / runtime / "AGENTS.md"
            self.assertEqual(agents.read_text(), (self.source / "AGENTS.md").read_text())
            skill = self.home / runtime / "skills" / "logging-observability"
            self.assertTrue(skill.is_dir())
            self.assertFalse(skill.is_symlink())
            self.assertEqual(
                (skill / "SKILL.md").read_text(),
                (self.source / ".agents/skills/logging-observability/SKILL.md").read_text(),
            )
            state = json.loads((self.home / runtime / ".personal-agent-harness.json").read_text())
            self.assertEqual(state["schema_version"], 2)
            self.assertIn("harness_version", state)
            self.assertIn("logging-observability/SKILL.md", state["skill_files"])

    def test_refuses_to_replace_unmanaged_agents_file(self):
        target = self.home / ".codex/AGENTS.md"
        target.parent.mkdir(parents=True)
        target.write_text("user-owned\n")

        with self.assertRaises(InstallConflict):
            Installer(self.source, self.home).install("codex")

        self.assertEqual(target.read_text(), "user-owned\n")

    def test_dry_run_does_not_write(self):
        actions = Installer(self.source, self.home, dry_run=True).install("all")
        self.assertGreater(len(actions), 0)
        self.assertFalse((self.home / ".codex").exists())
        self.assertFalse((self.home / ".claude").exists())

    def test_preflights_every_runtime_before_writing(self):
        conflict = self.home / ".claude/AGENTS.md"
        conflict.parent.mkdir(parents=True)
        conflict.write_text("user-owned\n")

        with self.assertRaises(InstallConflict):
            Installer(self.source, self.home).install("all")

        self.assertFalse((self.home / ".codex").exists())

    def test_refresh_removes_stale_managed_skill(self):
        Installer(self.source, self.home).install("codex")
        state_path = self.home / ".codex/.personal-agent-harness.json"
        state = json.loads(state_path.read_text())
        stale = self.home / ".codex/skills/removed-skill"
        stale.mkdir()
        (stale / "SKILL.md").write_text("managed old content\n")
        state["skills"].append("removed-skill")
        state["skill_files"]["removed-skill/SKILL.md"] = Installer.hash_bytes(
            b"managed old content\n"
        )
        state_path.write_text(json.dumps(state))

        Installer(self.source, self.home).install("codex")

        self.assertFalse(stale.exists())

    def test_uninstall_removes_only_unchanged_managed_files(self):
        installer = Installer(self.source, self.home)
        installer.install("codex")
        unrelated = self.home / ".codex/skills/user-skill"
        unrelated.mkdir()
        (unrelated / "SKILL.md").write_text("mine\n")

        installer.uninstall("codex")

        self.assertFalse((self.home / ".codex/AGENTS.md").exists())
        self.assertFalse((self.home / ".codex/skills/logging-observability").exists())
        self.assertTrue(unrelated.exists())

    def test_configures_claude_agents_mode_without_losing_settings(self):
        settings_path = self.home / ".claude/settings.json"
        settings_path.parent.mkdir(parents=True)
        settings_path.write_text(json.dumps({"theme": "dark"}))

        Installer(self.source, self.home).configure_claude_agents()

        settings = json.loads(settings_path.read_text())
        self.assertEqual(settings["theme"], "dark")
        self.assertEqual(
            settings["pluginConfigs"]["agents-md@builtin"]["options"]["instructionFiles"],
            "claude-md-and-agents-md",
        )

    def test_cli_mode_refuses_dirty_source(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source"
            shutil.copytree(self.source, source, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            subprocess.run(["git", "init", "-q", str(source)], check=True)
            subprocess.run(["git", "-C", str(source), "add", "--all"], check=True)
            subprocess.run(
                [
                    "git",
                    "-C",
                    str(source),
                    "-c",
                    "user.name=Harness Test",
                    "-c",
                    "user.email=harness@example.invalid",
                    "commit",
                    "-qm",
                    "fixture",
                ],
                check=True,
            )
            (source / "VERSION").write_text("9.9.9\n")

            with self.assertRaises(InstallConflict):
                Installer(source, self.home, require_clean=True).install("codex")


if __name__ == "__main__":
    unittest.main()
