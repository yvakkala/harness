#!/usr/bin/env python3
"""Diagnose runtime compatibility and installed harness integrity."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path

try:
    from scripts.install import Installer, RUNTIMES, STATE_NAME, file_sha256, tree_hashes
except ModuleNotFoundError:
    from install import Installer, RUNTIMES, STATE_NAME, file_sha256, tree_hashes


CLAUDE_AGENTS_MINIMUM = (2, 1, 277)


def parse_version(value: str) -> tuple[int, ...] | None:
    match = re.search(r"\b(\d+)\.(\d+)\.(\d+)\b", value)
    return tuple(map(int, match.groups())) if match else None


@dataclass(frozen=True)
class Finding:
    code: str
    ok: bool
    message: str
    remediation: str | None = None


class Doctor:
    def __init__(self, source: Path, home: Path):
        self.source = source.resolve()
        self.home = home.resolve()

    def runtime_version(self, name: str) -> str | None:
        executable = shutil.which(name)
        if not executable:
            return None
        result = subprocess.run(
            [executable, "--version"], text=True, capture_output=True, check=False
        )
        return (result.stdout or result.stderr).strip() or None

    def run(self) -> list[Finding]:
        findings: list[Finding] = []
        findings.extend(self._runtime_findings())
        for runtime, directory in RUNTIMES.items():
            findings.extend(self._installation_findings(runtime, self.home / directory))
        findings.append(self._claude_mode_finding())
        return findings

    def _runtime_findings(self) -> list[Finding]:
        findings: list[Finding] = []
        for runtime in RUNTIMES:
            raw = self.runtime_version(runtime)
            findings.append(
                Finding(
                    f"{runtime}-available",
                    raw is not None,
                    f"{runtime}: {raw}" if raw else f"{runtime} executable not found",
                    None if raw else f"Install {runtime} before using its harness adapter.",
                )
            )
            if runtime == "claude" and raw:
                version = parse_version(raw)
                supported = bool(version and version >= CLAUDE_AGENTS_MINIMUM)
                findings.append(
                    Finding(
                        "claude-version",
                        supported,
                        f"Claude Code {version} supports AGENTS.md"
                        if supported
                        else f"Claude Code {version} predates AGENTS.md support",
                        None if supported else "Run `claude update` and require version 2.1.277 or newer.",
                    )
                )
        return findings

    def _installation_findings(self, runtime: str, root: Path) -> list[Finding]:
        state_path = root / STATE_NAME
        state = Installer._read_state(state_path)
        if not state:
            return [
                Finding(
                    f"{runtime}-installation",
                    False,
                    f"No managed harness installation found in {root}",
                    f"Run `python scripts/install.py --target {runtime}`.",
                )
            ]
        agents = root / "AGENTS.md"
        agents_ok = agents.is_file() and not agents.is_symlink() and file_sha256(agents) == state.get(
            "agents_sha256"
        )
        findings = [
            Finding(
                f"{runtime}-agents-integrity",
                agents_ok,
                f"{runtime} AGENTS.md matches its installation manifest"
                if agents_ok
                else f"{runtime} AGENTS.md is missing or modified",
                None if agents_ok else f"Run the installer for {runtime}; it will preserve unmanaged edits.",
            )
        ]
        expected_files = state.get("skill_files", {})
        actual_files: dict[str, str] = {}
        for name in state.get("skills", []):
            skill = root / "skills" / name
            if skill.is_dir() and not skill.is_symlink():
                actual_files.update(
                    {f"{name}/{relative}": digest for relative, digest in tree_hashes(skill).items()}
                )
        skills_ok = bool(expected_files) and actual_files == expected_files
        findings.append(
            Finding(
                f"{runtime}-skills-integrity",
                skills_ok,
                f"{runtime} skill copies match their installation manifest"
                if skills_ok
                else f"{runtime} skills are missing, stale, linked, or modified",
                None if skills_ok else f"Run `python scripts/install.py --target {runtime}`.",
            )
        )
        return findings

    def _claude_mode_finding(self) -> Finding:
        path = self.home / ".claude/settings.json"
        try:
            settings = json.loads(path.read_text()) if path.exists() else {}
        except (json.JSONDecodeError, OSError):
            settings = {}
        mode = None
        plugin_configs = settings.get("pluginConfigs", {})
        if isinstance(plugin_configs, dict):
            agents_plugin = plugin_configs.get("agents-md@builtin", {})
            if isinstance(agents_plugin, dict):
                options = agents_plugin.get("options", {})
                if isinstance(options, dict):
                    mode = options.get("instructionFiles")
        ok = mode == "claude-md-and-agents-md"
        return Finding(
            "claude-instruction-mode",
            ok,
            "Claude loads AGENTS.md alongside repository CLAUDE.md files"
            if ok
            else f"Claude AGENTS.md mode is {mode or 'the fallback default'}",
            None
            if ok
            else "Set agents-md@builtin instructionFiles to claude-md-and-agents-md in ~/.claude/settings.json.",
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--home", type=Path, default=Path.home())
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    findings = Doctor(args.source, args.home).run()
    if args.json:
        print(json.dumps([asdict(finding) for finding in findings], indent=2))
    else:
        for finding in findings:
            print(f"{'PASS' if finding.ok else 'FAIL'} {finding.code}: {finding.message}")
            if finding.remediation and not finding.ok:
                print(f"  {finding.remediation}")
    return 0 if all(finding.ok for finding in findings) else 1


if __name__ == "__main__":
    raise SystemExit(main())
