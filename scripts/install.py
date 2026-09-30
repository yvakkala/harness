#!/usr/bin/env python3
"""Install, refresh, inspect, or remove the personal agent harness safely."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


RUNTIMES = {"codex": ".codex", "claude": ".claude"}
STATE_NAME = ".personal-agent-harness.json"
STATE_SCHEMA = 2


class InstallConflict(RuntimeError):
    """Raised when an operation would replace or remove an unmanaged file."""


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tree_hashes(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): file_sha256(path)
        for path in sorted(root.rglob("*"))
        if path.is_file() and not path.is_symlink()
    }


@dataclass
class RuntimePlan:
    name: str
    root: Path
    state_path: Path
    old_state: dict
    skill_sources: dict[str, Path]
    stale_skills: set[str]


@dataclass
class StagedRuntime:
    plan: RuntimePlan
    stage: Path
    backup: Path
    moved_to_backup: list[tuple[Path, Path]]
    activated: list[Path]


class Installer:
    def __init__(
        self, source: Path, home: Path, dry_run: bool = False, require_clean: bool = False
    ):
        self.source = source.resolve()
        self.home = home.resolve()
        self.dry_run = dry_run
        self.require_clean = require_clean
        self.actions: list[str] = []

    @staticmethod
    def hash_bytes(content: bytes) -> str:
        return hashlib.sha256(content).hexdigest()

    def install(self, target: str) -> list[str]:
        runtimes = self._runtime_names(target)
        self._validate_source()
        plans = [self._preflight(runtime) for runtime in runtimes]
        for plan in plans:
            self._describe_install(plan)
        if self.dry_run:
            return self.actions

        staged: list[StagedRuntime] = []
        try:
            for plan in plans:
                staged.append(self._stage(plan))
            for item in staged:
                self._activate(item)
        except Exception:
            for item in reversed(staged):
                self._rollback(item)
            raise
        else:
            for item in staged:
                shutil.rmtree(item.backup, ignore_errors=True)
                shutil.rmtree(item.stage, ignore_errors=True)
        return self.actions

    def uninstall(self, target: str) -> list[str]:
        plans = [self._preflight_uninstall(runtime) for runtime in self._runtime_names(target)]
        for plan in plans:
            self.actions.append(f"remove managed files from {plan.root}")
        if self.dry_run:
            return self.actions
        for plan in plans:
            agents = plan.root / "AGENTS.md"
            if agents.exists() or agents.is_symlink():
                self._remove_path(agents)
            for name in plan.old_state.get("skills", []):
                skill = plan.root / "skills" / name
                if skill.exists() or skill.is_symlink():
                    self._remove_path(skill)
            if plan.state_path.exists():
                plan.state_path.unlink()
        return self.actions

    def status(self, target: str) -> dict[str, dict]:
        result: dict[str, dict] = {}
        for runtime in self._runtime_names(target):
            root = self.home / RUNTIMES[runtime]
            state = self._read_state(root / STATE_NAME)
            result[runtime] = {
                "installed": bool(state),
                "root": str(root),
                "harness_version": state.get("harness_version"),
                "source_commit": state.get("source_commit"),
                "skills": state.get("skills", []),
            }
        return result

    def configure_claude_agents(self) -> str:
        """Enable AGENTS.md alongside CLAUDE.md while preserving other Claude settings."""
        path = self.home / ".claude/settings.json"
        if path.exists():
            try:
                settings = json.loads(path.read_text())
            except json.JSONDecodeError as exc:
                raise InstallConflict(f"Refusing to edit invalid Claude settings: {path}") from exc
            if not isinstance(settings, dict):
                raise InstallConflict(f"Refusing to edit invalid Claude settings: {path}")
        else:
            settings = {}
        plugin_configs = settings.setdefault("pluginConfigs", {})
        if not isinstance(plugin_configs, dict):
            raise InstallConflict("Claude setting pluginConfigs must be an object")
        agents_plugin = plugin_configs.setdefault("agents-md@builtin", {})
        if not isinstance(agents_plugin, dict):
            raise InstallConflict("Claude setting agents-md@builtin must be an object")
        options = agents_plugin.setdefault("options", {})
        if not isinstance(options, dict):
            raise InstallConflict("Claude agents-md options must be an object")
        options["instructionFiles"] = "claude-md-and-agents-md"
        action = f"configure Claude to load AGENTS.md alongside CLAUDE.md in {path}"
        if self.dry_run:
            return action
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_name(f".{path.name}.harness-tmp")
        temporary.write_text(json.dumps(settings, indent=2, sort_keys=True) + "\n")
        os.replace(temporary, path)
        return action

    def _runtime_names(self, target: str) -> list[str]:
        runtimes = list(RUNTIMES) if target == "all" else [target]
        if any(runtime not in RUNTIMES for runtime in runtimes):
            raise ValueError(f"Unsupported target: {target}")
        return runtimes

    def _validate_source(self) -> None:
        for path in (self.source / "AGENTS.md", self.source / "VERSION"):
            if not path.is_file():
                raise FileNotFoundError(path)
        skill_root = self.source / ".agents/skills"
        if not skill_root.is_dir():
            raise FileNotFoundError(skill_root)
        if not list(skill_root.glob("*/SKILL.md")):
            raise InstallConflict("No skills found in source")
        try:
            from scripts.validate import validate_repository
        except ModuleNotFoundError:
            from validate import validate_repository
        validation_errors = validate_repository(self.source)
        if validation_errors:
            raise InstallConflict(
                "Source validation failed: " + "; ".join(validation_errors[:5])
            )
        if self.require_clean:
            result = subprocess.run(
                ["git", "-C", str(self.source), "status", "--porcelain"],
                text=True,
                capture_output=True,
                check=False,
            )
            if result.returncode == 0 and result.stdout.strip():
                raise InstallConflict(
                    "Refusing to install from a dirty source; commit changes or use --allow-dirty"
                )

    def _preflight(self, runtime: str) -> RuntimePlan:
        root = self.home / RUNTIMES[runtime]
        state_path = root / STATE_NAME
        old_state = self._read_state(state_path)
        self._check_agents_target(root / "AGENTS.md", old_state)
        skill_sources = {
            path.name: path
            for path in sorted((self.source / ".agents/skills").iterdir())
            if path.is_dir()
        }
        old_skills = set(old_state.get("skills", []))
        for name, source in skill_sources.items():
            self._check_skill_target(root / "skills" / name, source, old_state)
        stale_skills = old_skills - set(skill_sources)
        for name in stale_skills:
            self._check_skill_target(root / "skills" / name, None, old_state)
        return RuntimePlan(runtime, root, state_path, old_state, skill_sources, stale_skills)

    def _preflight_uninstall(self, runtime: str) -> RuntimePlan:
        root = self.home / RUNTIMES[runtime]
        state_path = root / STATE_NAME
        state = self._read_state(state_path)
        if not state:
            return RuntimePlan(runtime, root, state_path, {}, {}, set())
        self._check_agents_target(root / "AGENTS.md", state, uninstall=True)
        for name in state.get("skills", []):
            self._check_skill_target(root / "skills" / name, None, state)
        return RuntimePlan(runtime, root, state_path, state, {}, set(state.get("skills", [])))

    def _describe_install(self, plan: RuntimePlan) -> None:
        self.actions.append(f"copy {self.source / 'AGENTS.md'} -> {plan.root / 'AGENTS.md'}")
        for name, source in plan.skill_sources.items():
            self.actions.append(f"copy {source} -> {plan.root / 'skills' / name}")
        for name in sorted(plan.stale_skills):
            self.actions.append(f"remove stale managed skill {plan.root / 'skills' / name}")

    def _stage(self, plan: RuntimePlan) -> StagedRuntime:
        plan.root.mkdir(parents=True, exist_ok=True)
        stage = Path(tempfile.mkdtemp(prefix=".harness-stage-", dir=plan.root))
        backup = Path(tempfile.mkdtemp(prefix=".harness-backup-", dir=plan.root))
        shutil.copy2(self.source / "AGENTS.md", stage / "AGENTS.md")
        stage_skills = stage / "skills"
        stage_skills.mkdir()
        for name, source in plan.skill_sources.items():
            shutil.copytree(source, stage_skills / name, symlinks=False)
        state = self._build_state(plan.skill_sources)
        (stage / STATE_NAME).write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")
        return StagedRuntime(plan, stage, backup, [], [])

    def _activate(self, item: StagedRuntime) -> None:
        plan = item.plan
        (plan.root / "skills").mkdir(exist_ok=True)
        targets = [plan.root / "AGENTS.md", plan.state_path]
        targets.extend(plan.root / "skills" / name for name in plan.skill_sources)
        targets.extend(plan.root / "skills" / name for name in plan.stale_skills)
        for target in targets:
            if target.exists() or target.is_symlink():
                backup_target = item.backup / target.relative_to(plan.root)
                backup_target.parent.mkdir(parents=True, exist_ok=True)
                os.replace(target, backup_target)
                item.moved_to_backup.append((target, backup_target))

        replacements = [
            (item.stage / "AGENTS.md", plan.root / "AGENTS.md"),
            (item.stage / STATE_NAME, plan.state_path),
        ]
        replacements.extend(
            (item.stage / "skills" / name, plan.root / "skills" / name)
            for name in plan.skill_sources
        )
        for staged_path, target in replacements:
            os.replace(staged_path, target)
            item.activated.append(target)

    def _rollback(self, item: StagedRuntime) -> None:
        for target in reversed(item.activated):
            if target.exists() or target.is_symlink():
                self._remove_path(target)
        for target, backup in reversed(item.moved_to_backup):
            if backup.exists() or backup.is_symlink():
                target.parent.mkdir(parents=True, exist_ok=True)
                os.replace(backup, target)
        shutil.rmtree(item.stage, ignore_errors=True)
        shutil.rmtree(item.backup, ignore_errors=True)

    def _build_state(self, skill_sources: dict[str, Path]) -> dict:
        skill_files: dict[str, str] = {}
        for name, source in skill_sources.items():
            for relative, digest in tree_hashes(source).items():
                skill_files[f"{name}/{relative}"] = digest
        return {
            "schema_version": STATE_SCHEMA,
            "harness_version": (self.source / "VERSION").read_text().strip(),
            "source": str(self.source),
            "source_commit": self._source_commit(),
            "agents_sha256": file_sha256(self.source / "AGENTS.md"),
            "skills": sorted(skill_sources),
            "skill_files": skill_files,
        }

    def _source_commit(self) -> str | None:
        result = subprocess.run(
            ["git", "-C", str(self.source), "rev-parse", "HEAD"],
            text=True,
            capture_output=True,
            check=False,
        )
        return result.stdout.strip() if result.returncode == 0 else None

    def _check_agents_target(self, target: Path, old_state: dict, uninstall: bool = False) -> None:
        if not target.exists() and not target.is_symlink():
            return
        if target.is_symlink() or not target.is_file():
            raise InstallConflict(f"Refusing to replace unexpected AGENTS target: {target}")
        current_hash = file_sha256(target)
        accepted = {old_state.get("agents_sha256")}
        if not uninstall:
            accepted.add(file_sha256(self.source / "AGENTS.md"))
        if current_hash not in accepted:
            raise InstallConflict(f"Refusing to replace unmanaged or edited file: {target}")

    def _check_skill_target(self, target: Path, source: Path | None, old_state: dict) -> None:
        if not target.exists() and not target.is_symlink():
            return
        old_skills = set(old_state.get("skills", []))
        if target.name not in old_skills:
            raise InstallConflict(f"Refusing to replace existing skill: {target}")
        if target.is_symlink():
            old_source = old_state.get("source")
            allowed = []
            if source is not None:
                allowed.append(source.resolve())
            if old_source:
                allowed.append((Path(old_source) / ".agents/skills" / target.name).resolve())
            if target.resolve() not in allowed:
                raise InstallConflict(f"Managed skill link changed unexpectedly: {target}")
            return
        if not target.is_dir():
            raise InstallConflict(f"Managed skill is not a directory: {target}")
        expected = {
            key.split("/", 1)[1]: value
            for key, value in old_state.get("skill_files", {}).items()
            if key.startswith(f"{target.name}/")
        }
        if not expected or tree_hashes(target) != expected:
            raise InstallConflict(f"Refusing to replace edited managed skill: {target}")

    @staticmethod
    def _read_state(path: Path) -> dict:
        if not path.is_file():
            return {}
        try:
            data = json.loads(path.read_text())
        except (json.JSONDecodeError, OSError) as exc:
            raise InstallConflict(f"Cannot trust invalid installer state: {path}") from exc
        if not isinstance(data, dict):
            raise InstallConflict(f"Cannot trust invalid installer state: {path}")
        return data

    @staticmethod
    def _remove_path(path: Path) -> None:
        if path.is_symlink() or path.is_file():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(path)


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source", type=Path, default=Path(__file__).resolve().parents[1], help="Harness root"
    )
    parser.add_argument("--home", type=Path, default=Path.home(), help="Target home directory")
    parser.add_argument("--target", choices=["all", *RUNTIMES], default="all")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--allow-dirty",
        action="store_true",
        help="Allow installing uncommitted source for deliberate local development",
    )
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--uninstall", action="store_true")
    action.add_argument("--status", action="store_true")
    parser.add_argument(
        "--configure-claude-agents",
        action="store_true",
        help="Preserve Claude settings and load AGENTS.md alongside CLAUDE.md",
    )
    return parser.parse_args(argv)


def main() -> int:
    args = parse_args()
    installer = Installer(
        args.source, args.home, args.dry_run, require_clean=not args.allow_dirty
    )
    try:
        if args.status:
            print(json.dumps(installer.status(args.target), indent=2, sort_keys=True))
            return 0
        actions = installer.uninstall(args.target) if args.uninstall else installer.install(args.target)
        if args.configure_claude_agents and not args.uninstall:
            actions.append(installer.configure_claude_agents())
    except (InstallConflict, FileNotFoundError, OSError, ValueError) as exc:
        print(f"install error: {exc}", file=sys.stderr)
        return 1
    for action in actions:
        print(action)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
