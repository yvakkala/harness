#!/usr/bin/env python3
"""Install the shared AGENTS.md and skill catalog without overwriting user files."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from typing import Iterable


RUNTIMES = {"codex": ".codex", "claude": ".claude"}
STATE_NAME = ".personal-agent-harness.json"


class InstallConflict(RuntimeError):
    """Raised when installation would replace an unmanaged or edited file."""


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Installer:
    def __init__(self, source: Path, home: Path, dry_run: bool = False):
        self.source = source.resolve()
        self.home = home.resolve()
        self.dry_run = dry_run
        self.actions: list[str] = []

    def install(self, target: str) -> list[str]:
        runtimes = list(RUNTIMES) if target == "all" else [target]
        if any(runtime not in RUNTIMES for runtime in runtimes):
            raise ValueError(f"Unsupported target: {target}")
        self._validate_source()
        for runtime in runtimes:
            self._install_runtime(runtime)
        return self.actions

    def _validate_source(self) -> None:
        if not (self.source / "AGENTS.md").is_file():
            raise FileNotFoundError(self.source / "AGENTS.md")
        if not (self.source / ".agents/skills").is_dir():
            raise FileNotFoundError(self.source / ".agents/skills")

    def _install_runtime(self, runtime: str) -> None:
        runtime_root = self.home / RUNTIMES[runtime]
        agents_target = runtime_root / "AGENTS.md"
        state_path = runtime_root / STATE_NAME
        old_state = self._read_state(state_path)
        self._check_agents_target(agents_target, old_state)

        skill_sources = sorted(
            path for path in (self.source / ".agents/skills").iterdir() if path.is_dir()
        )
        for skill_source in skill_sources:
            self._check_skill_target(runtime_root / "skills" / skill_source.name, skill_source)

        self.actions.append(f"copy {self.source / 'AGENTS.md'} -> {agents_target}")
        for skill_source in skill_sources:
            self.actions.append(
                f"link {runtime_root / 'skills' / skill_source.name} -> {skill_source}"
            )
        if self.dry_run:
            return

        runtime_root.mkdir(parents=True, exist_ok=True)
        self._atomic_write(agents_target, (self.source / "AGENTS.md").read_bytes())
        skills_target = runtime_root / "skills"
        skills_target.mkdir(parents=True, exist_ok=True)
        for skill_source in skill_sources:
            skill_target = skills_target / skill_source.name
            if skill_target.is_symlink():
                if skill_target.resolve() == skill_source.resolve():
                    continue
                skill_target.unlink()
            os.symlink(skill_source, skill_target, target_is_directory=True)

        state = {
            "source": str(self.source),
            "agents_sha256": file_sha256(self.source / "AGENTS.md"),
            "skills": [skill.name for skill in skill_sources],
        }
        self._atomic_write(state_path, (json.dumps(state, indent=2) + "\n").encode())

    def _check_agents_target(self, target: Path, old_state: dict) -> None:
        if not target.exists():
            return
        current_hash = file_sha256(target)
        source_hash = file_sha256(self.source / "AGENTS.md")
        previous_hash = old_state.get("agents_sha256")
        if current_hash not in {source_hash, previous_hash}:
            raise InstallConflict(f"Refusing to replace unmanaged or edited file: {target}")

    @staticmethod
    def _check_skill_target(target: Path, source: Path) -> None:
        if target.is_symlink() and target.resolve() == source.resolve():
            return
        if target.exists() or target.is_symlink():
            raise InstallConflict(f"Refusing to replace existing skill: {target}")

    @staticmethod
    def _read_state(path: Path) -> dict:
        if not path.is_file():
            return {}
        try:
            data = json.loads(path.read_text())
        except (json.JSONDecodeError, OSError) as exc:
            raise InstallConflict(f"Cannot trust invalid installer state: {path}") from exc
        return data if isinstance(data, dict) else {}

    @staticmethod
    def _atomic_write(path: Path, content: bytes) -> None:
        temporary = path.with_name(f".{path.name}.tmp")
        temporary.write_bytes(content)
        os.replace(temporary, path)


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Harness repository root",
    )
    parser.add_argument("--home", type=Path, default=Path.home(), help="Target home directory")
    parser.add_argument("--target", choices=["all", *RUNTIMES], default="all")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def main() -> int:
    args = parse_args()
    try:
        actions = Installer(args.source, args.home, args.dry_run).install(args.target)
    except (InstallConflict, FileNotFoundError, ValueError) as exc:
        print(f"install error: {exc}")
        return 1
    for action in actions:
        print(action)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
