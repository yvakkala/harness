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

    def test_installs_shared_agents_and_skill_links_for_both_runtimes(self):
        Installer(self.source, self.home).install("all")

        for runtime in (".codex", ".claude"):
            agents = self.home / runtime / "AGENTS.md"
            self.assertEqual(agents.read_text(), (self.source / "AGENTS.md").read_text())
            skill = self.home / runtime / "skills" / "logging-observability"
            self.assertTrue(skill.is_symlink())
            self.assertEqual(skill.resolve(), self.source / ".agents/skills/logging-observability")

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


if __name__ == "__main__":
    unittest.main()
