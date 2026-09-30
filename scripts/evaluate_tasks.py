#!/usr/bin/env python3
"""Run sandboxed fixture tasks and grade resulting filesystem state."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path


def workspace_hashes(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*"))
        if path.is_file() and ".git" not in path.parts
    }


def build_task_command(provider: str, workspace: Path) -> list[str]:
    if provider == "codex":
        return [
            "codex",
            "exec",
            "--json",
            "--ephemeral",
            "--sandbox",
            "workspace-write",
            "--skip-git-repo-check",
            "--cd",
            str(workspace),
            "-",
        ]
    if provider == "claude":
        return [
            "claude",
            "-p",
            "--output-format",
            "stream-json",
            "--verbose",
            "--permission-mode",
            "acceptEdits",
            "--allowedTools",
            "Read,Edit,Write",
            "--disallowedTools",
            "Bash,WebFetch,WebSearch",
            "--no-session-persistence",
        ]
    raise ValueError(f"unsupported provider: {provider}")


def _json_pointer(value, pointer: list[str]):
    current = value
    for segment in pointer:
        if isinstance(current, list):
            current = current[int(segment)]
        else:
            current = current[segment]
    return current


def grade_workspace(task: dict, workspace: Path, before: dict[str, str]) -> dict:
    failures: list[str] = []
    after = workspace_hashes(workspace)
    changed = sorted(
        path for path in set(before) | set(after) if before.get(path) != after.get(path)
    )
    unexpected = sorted(set(changed) - set(task.get("allowed_changes", [])))
    if unexpected:
        failures.append(f"unexpected changed files: {unexpected}")
    for check in task.get("checks", []):
        path = workspace / check["path"]
        if check["type"] == "file_exists":
            if not path.is_file():
                failures.append(f"missing file: {check['path']}")
            continue
        if check["type"] == "json_value":
            try:
                value = _json_pointer(json.loads(path.read_text()), check.get("pointer", []))
            except (OSError, json.JSONDecodeError, KeyError, IndexError, ValueError) as exc:
                failures.append(f"cannot read {check['path']} at {check.get('pointer', [])}: {exc}")
                continue
            if value != check.get("equals"):
                failures.append(
                    f"{check['path']} {check.get('pointer', [])} expected "
                    f"{check.get('equals')!r}, got {value!r}"
                )
            continue
        failures.append(f"unsupported check type: {check['type']}")
    return {"passed": not failures, "failures": failures, "changed_files": changed}


def run_trial(provider: str, task: dict, fixtures: Path, artifacts: Path, timeout: int, trial: int) -> dict:
    fixture = fixtures / task["fixture"]
    with tempfile.TemporaryDirectory(prefix=f"harness-eval-{task['id']}-") as directory:
        workspace = Path(directory) / "workspace"
        shutil.copytree(fixture, workspace)
        before = workspace_hashes(workspace)
        started = time.monotonic()
        result = subprocess.run(
            build_task_command(provider, workspace),
            input=task["prompt"],
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
        score = grade_workspace(task, workspace, before)
        run_dir = artifacts / task["id"] / f"trial-{trial}"
        run_dir.mkdir(parents=True, exist_ok=True)
        (run_dir / "stdout.jsonl").write_text(result.stdout)
        (run_dir / "stderr.txt").write_text(result.stderr)
        shutil.copytree(workspace, run_dir / "workspace")
        return {
            "provider": provider,
            "task_id": task["id"],
            "trial": trial,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "duration_seconds": round(time.monotonic() - started, 3),
            "exit_code": result.returncode,
            "score": score,
        }


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", choices=["codex", "claude"], required=True)
    parser.add_argument("--task")
    parser.add_argument("--trials", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--output", type=Path, default=root / "evals/artifacts/tasks")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    tasks = json.loads((root / "evals/tasks.json").read_text())
    if args.task:
        tasks = [task for task in tasks if task["id"] == args.task]
    if not tasks:
        parser.error("no matching tasks")
    if args.trials < 1:
        parser.error("--trials must be positive")
    if args.dry_run:
        for task in tasks:
            fixture = root / "evals/fixtures" / task["fixture"]
            if not fixture.is_dir():
                parser.error(f"missing fixture: {fixture}")
        print(f"Prepared {len(tasks)} fixture tasks for {args.provider} x {args.trials} trial(s).")
        return 0

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    artifacts = args.output / f"{args.provider}-{stamp}"
    records = []
    for task in tasks:
        for trial in range(1, args.trials + 1):
            records.append(
                run_trial(
                    args.provider,
                    task,
                    root / "evals/fixtures",
                    artifacts,
                    args.timeout,
                    trial,
                )
            )
    report = artifacts / "report.json"
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps(records, indent=2) + "\n")
    passed = sum(record["exit_code"] == 0 and record["score"]["passed"] for record in records)
    print(f"{passed}/{len(records)} fixture trials passed; report: {report}")
    return 0 if passed == len(records) else 1


if __name__ == "__main__":
    raise SystemExit(main())
