#!/usr/bin/env python3
"""Validate the compact instruction file, skill catalog, coverage, and eval suites."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    from scripts.update_manifest import build_manifest
except ModuleNotFoundError:
    from update_manifest import build_manifest


FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
FIELD = re.compile(r"^([a-zA-Z0-9_-]+):\s*(.+?)\s*$")
SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")
REQUIREMENT_ID = re.compile(r"^#### ([A-Z]+)-\d+ —", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
BEHAVIOR_FIELDS = {
    "id": str,
    "prompt": str,
    "expected_skills": list,
    "expected": list,
    "forbidden": list,
}
ROUTING_FIELDS = {
    "id": str,
    "prompt": str,
    "expected_action": str,
    "expected_skills": list,
    "forbidden_skills": list,
}
TASK_FIELDS = {
    "id": str,
    "fixture": str,
    "prompt": str,
    "allowed_changes": list,
    "checks": list,
}


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(errors="replace")
    match = FRONTMATTER.match(text)
    if not match:
        return {}
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        field = FIELD.match(line)
        if field:
            result[field.group(1)] = field.group(2).strip('"\'')
    return result


def _validate_case(case: object, index: int, fields: dict[str, type], errors: list[str]) -> str | None:
    label = f"evaluation case {index + 1}"
    if not isinstance(case, dict):
        errors.append(f"{label} must be an object")
        return None
    for field, expected_type in fields.items():
        value = case.get(field)
        allow_empty = field in {"expected_skills", "forbidden_skills"}
        if not isinstance(value, expected_type) or (not allow_empty and not value):
            errors.append(f"{label} needs {field!r} of type {expected_type.__name__}")
    for field in ("expected_skills", "forbidden_skills", "expected", "forbidden"):
        value = case.get(field)
        if isinstance(value, list) and not all(isinstance(item, str) and item.strip() for item in value):
            errors.append(f"{label} field {field!r} must contain strings")
    return case.get("id") if isinstance(case.get("id"), str) else None


def _validate_markdown_links(root: Path, errors: list[str]) -> None:
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for target in MARKDOWN_LINK.findall(path.read_text(errors="replace")):
            target = target.strip("<>").split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"broken relative link in {path.relative_to(root)}: {target}")


def validate_repository(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    agents = root / "AGENTS.md"
    if not agents.is_file():
        errors.append("AGENTS.md is missing")
    else:
        line_count = len(agents.read_text(errors="replace").splitlines())
        if line_count > 200:
            errors.append(f"AGENTS.md has {line_count} lines; maximum is 200")

    version = root / "VERSION"
    if not version.is_file() or not SEMVER.fullmatch(version.read_text().strip()):
        errors.append("VERSION is missing or is not semantic version syntax")
    if not (root / "CHANGELOG.md").is_file():
        errors.append("CHANGELOG.md is missing")

    for path in root.rglob("CLAUDE.md"):
        if ".git" not in path.parts:
            errors.append(f"provider-specific instruction file is prohibited: {path.relative_to(root)}")

    skill_root = root / ".agents/skills"
    names: set[str] = set()
    if not skill_root.is_dir():
        errors.append(".agents/skills is missing")
        return errors

    for path in skill_root.rglob("*"):
        if path.is_symlink():
            errors.append(f"skill catalog may not contain symlinks: {path.relative_to(root)}")

    for directory in sorted(path for path in skill_root.iterdir() if path.is_dir()):
        skill_file = directory / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"missing SKILL.md: {directory.relative_to(root)}")
            continue
        text = skill_file.read_text(errors="replace")
        if "TODO" in text or "[TODO" in text:
            errors.append(f"unfinished skill scaffold: {skill_file.relative_to(root)}")
        if len(text.splitlines()) > 500:
            errors.append(f"skill exceeds 500 lines: {skill_file.relative_to(root)}")
        metadata = parse_frontmatter(skill_file)
        name = metadata.get("name", "")
        description = metadata.get("description", "")
        if not SKILL_NAME.fullmatch(name) or "--" in name or len(name) > 64:
            errors.append(f"invalid skill name in {skill_file.relative_to(root)}: {name!r}")
        if name != directory.name:
            errors.append(f"skill folder/name mismatch: {directory.name!r} versus {name!r}")
        if name in names:
            errors.append(f"duplicate skill name: {name}")
        names.add(name)
        if not description or len(description) > 1024:
            errors.append(f"invalid description in {skill_file.relative_to(root)}")
        if not (directory / "agents/openai.yaml").is_file():
            errors.append(f"missing OpenAI interface metadata: {directory.relative_to(root)}")

    lock_path = root / "skills.lock.json"
    if not lock_path.is_file():
        errors.append("skills.lock.json is missing")
    else:
        try:
            actual_manifest = json.loads(lock_path.read_text())
        except json.JSONDecodeError as exc:
            errors.append(f"invalid skill manifest JSON: {exc}")
        else:
            if actual_manifest != build_manifest(root):
                errors.append("skill manifest is stale or does not match catalog contents")

    all_identifiers: list[str] = []
    for filename, fields in (("cases.json", BEHAVIOR_FIELDS), ("routing.json", ROUTING_FIELDS)):
        eval_file = root / "evals" / filename
        if not eval_file.exists():
            errors.append(f"missing evaluation suite: evals/{filename}")
            continue
        try:
            cases = json.loads(eval_file.read_text())
        except json.JSONDecodeError as exc:
            errors.append(f"invalid eval JSON in {filename}: {exc}")
            continue
        if not isinstance(cases, list) or not cases:
            errors.append(f"evaluation cases in {filename} must be a non-empty array")
            continue
        for index, case in enumerate(cases):
            identifier = _validate_case(case, index, fields, errors)
            if identifier:
                all_identifiers.append(identifier)
    task_file = root / "evals/tasks.json"
    if not task_file.is_file():
        errors.append("missing evaluation suite: evals/tasks.json")
    else:
        try:
            tasks = json.loads(task_file.read_text())
        except json.JSONDecodeError as exc:
            errors.append(f"invalid eval JSON in tasks.json: {exc}")
        else:
            if not isinstance(tasks, list) or not tasks:
                errors.append("evaluation tasks must be a non-empty array")
            else:
                for index, task in enumerate(tasks):
                    identifier = _validate_case(task, index, TASK_FIELDS, errors)
                    if identifier:
                        all_identifiers.append(identifier)
                    if isinstance(task, dict):
                        fixture = task.get("fixture")
                        if isinstance(fixture, str) and not (
                            root / "evals/fixtures" / fixture
                        ).is_dir():
                            errors.append(f"evaluation case {index + 1} fixture is missing: {fixture}")
                        for check in task.get("checks", []):
                            if not isinstance(check, dict) or check.get("type") not in {
                                "file_exists",
                                "json_value",
                            }:
                                errors.append(f"evaluation case {index + 1} has an invalid task check")
    if len(all_identifiers) != len(set(all_identifiers)):
        errors.append("duplicate evaluation case id")

    requirements = root / "docs/personalized-requirements.md"
    if requirements.exists():
        required_groups = set(REQUIREMENT_ID.findall(requirements.read_text(errors="replace")))
        coverage_path = root / "docs/coverage.json"
        if not coverage_path.is_file():
            errors.append("docs/coverage.json is missing")
        else:
            try:
                coverage = json.loads(coverage_path.read_text())
            except json.JSONDecodeError as exc:
                errors.append(f"invalid coverage JSON: {exc}")
            else:
                covered_groups = set(coverage.get("requirement_groups", {})) if isinstance(coverage, dict) else set()
                if required_groups != covered_groups:
                    errors.append(
                        "coverage groups differ from requirements: "
                        f"missing={sorted(required_groups - covered_groups)}, "
                        f"extra={sorted(covered_groups - required_groups)}"
                    )

    _validate_markdown_links(root, errors)
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_repository(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    skill_count = len(list((root / ".agents/skills").glob("*/SKILL.md")))
    line_count = len((root / "AGENTS.md").read_text().splitlines())
    print(f"Validated AGENTS.md ({line_count} lines), {skill_count} skills, and evaluation suites.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
