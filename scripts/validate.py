#!/usr/bin/env python3
"""Validate the compact instruction file and provider-neutral skill catalog."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
FIELD = re.compile(r"^([a-zA-Z0-9_-]+):\s*(.+?)\s*$")
SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EVAL_REQUIRED_FIELDS = {
    "id": str,
    "prompt": str,
    "expected_skills": list,
    "expected": list,
    "forbidden": list,
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

    claude_files = [path for path in root.rglob("CLAUDE.md") if ".git" not in path.parts]
    for path in claude_files:
        errors.append(f"provider-specific instruction file is prohibited: {path.relative_to(root)}")

    skill_root = root / ".agents/skills"
    names: set[str] = set()
    if not skill_root.is_dir():
        errors.append(".agents/skills is missing")
        return errors

    for directory in sorted(path for path in skill_root.iterdir() if path.is_dir()):
        skill_file = directory / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"missing SKILL.md: {directory.relative_to(root)}")
            continue
        text = skill_file.read_text(errors="replace")
        if "TODO" in text or "[TODO" in text:
            errors.append(f"unfinished skill scaffold: {skill_file.relative_to(root)}")
        metadata = parse_frontmatter(skill_file)
        name = metadata.get("name", "")
        description = metadata.get("description", "")
        if not SKILL_NAME.fullmatch(name):
            errors.append(f"invalid skill name in {skill_file.relative_to(root)}: {name!r}")
        if name != directory.name:
            errors.append(
                f"skill folder/name mismatch: {directory.name!r} versus {name!r}"
            )
        if name in names:
            errors.append(f"duplicate skill name: {name}")
        names.add(name)
        if not description or len(description) > 1024:
            errors.append(f"invalid description in {skill_file.relative_to(root)}")

    eval_file = root / "evals/cases.json"
    if eval_file.exists():
        try:
            cases = json.loads(eval_file.read_text())
        except json.JSONDecodeError as exc:
            errors.append(f"invalid eval JSON: {exc}")
        else:
            if not isinstance(cases, list) or not cases:
                errors.append("evaluation cases must be a non-empty array")
            else:
                identifiers: list[str] = []
                for index, case in enumerate(cases):
                    label = f"evaluation case {index + 1}"
                    if not isinstance(case, dict):
                        errors.append(f"{label} must be an object")
                        continue
                    for field, expected_type in EVAL_REQUIRED_FIELDS.items():
                        value = case.get(field)
                        missing_or_empty = value is None or (
                            field != "expected_skills" and not value
                        )
                        if not isinstance(value, expected_type) or missing_or_empty:
                            errors.append(
                                f"{label} needs {field!r} of type "
                                f"{expected_type.__name__}"
                            )
                    identifier = case.get("id")
                    if isinstance(identifier, str) and identifier:
                        identifiers.append(identifier)
                    for field in ("expected_skills", "expected", "forbidden"):
                        value = case.get(field)
                        if isinstance(value, list) and not all(
                            isinstance(item, str) and item.strip() for item in value
                        ):
                            errors.append(f"{label} field {field!r} must contain strings")
                if len(identifiers) != len(set(identifiers)):
                    errors.append("duplicate evaluation case id")
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
    print(f"Validated AGENTS.md ({line_count} lines) and {skill_count} skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
