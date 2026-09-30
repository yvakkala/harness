#!/usr/bin/env python3
"""Regenerate the reviewed skill provenance and integrity manifest."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from scripts.install import tree_hashes
except ModuleNotFoundError:
    from install import tree_hashes


SUPERPOWERS_REVISION = "8ca22dba9a94f28898bbce59f2537ff4d87c747d"


def build_manifest(root: Path) -> dict:
    skills = {}
    for directory in sorted((root / ".agents/skills").iterdir()):
        if not directory.is_dir():
            continue
        adapted = directory.name == "systematic-debugging"
        skills[directory.name] = {
            "source": "https://github.com/obra/superpowers"
            if adapted
            else "local",
            "revision": SUPERPOWERS_REVISION if adapted else None,
            "license": "MIT; see LICENSE.txt" if adapted else "unlicensed",
            "files": tree_hashes(directory),
        }
    return {"schema_version": 1, "skills": skills}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    path = args.root / "skills.lock.json"
    expected = json.dumps(build_manifest(args.root), indent=2, sort_keys=True) + "\n"
    if args.check:
        if not path.exists() or path.read_text() != expected:
            print("skills.lock.json is stale; run python scripts/update_manifest.py")
            return 1
        print("Skill manifest is current.")
        return 0
    path.write_text(expected)
    print(f"Updated {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
