#!/usr/bin/env python3
"""Run repeatable read-only routing evaluations against Codex or Claude."""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path


def load_cases(directory: Path, suite: str | None = None) -> list[dict]:
    files = [directory / f"{suite}.json"] if suite else sorted(directory.glob("*.json"))
    cases: list[dict] = []
    for path in files:
        if path.name.endswith(".schema.json") or not path.exists():
            continue
        data = json.loads(path.read_text())
        if not isinstance(data, list):
            continue
        cases.extend(data)
    identifiers = [case.get("id") for case in cases]
    if len(identifiers) != len(set(identifiers)):
        raise ValueError("duplicate evaluation case id across suites")
    return cases


def build_command(provider: str, workdir: Path, schema: Path) -> list[str]:
    if provider == "codex":
        return [
            "codex",
            "exec",
            "--json",
            "--ephemeral",
            "--sandbox",
            "read-only",
            "--skip-git-repo-check",
            "--cd",
            str(workdir),
            "--output-schema",
            str(schema),
            "-",
        ]
    if provider == "claude":
        schema_text = schema.read_text() if schema.exists() else "{}"
        return [
            "claude",
            "-p",
            "--output-format",
            "stream-json",
            "--verbose",
            "--permission-mode",
            "plan",
            "--no-session-persistence",
            "--json-schema",
            schema_text,
        ]
    raise ValueError(f"unsupported provider: {provider}")


def score_decision(case: dict, decision: dict) -> dict:
    failures: list[str] = []
    expected_action = case.get("expected_action")
    if expected_action and decision.get("action") != expected_action:
        failures.append(f"expected action {expected_action!r}, got {decision.get('action')!r}")
    actual_skills = set(decision.get("skills", []))
    missing = set(case.get("expected_skills", [])) - actual_skills
    forbidden = set(case.get("forbidden_skills", [])) & actual_skills
    if missing:
        failures.append(f"missing skills: {sorted(missing)}")
    if forbidden:
        failures.append(f"forbidden skills: {sorted(forbidden)}")
    return {"passed": not failures, "failures": failures}


def decision_prompt(case: dict) -> str:
    return f"""You are evaluating the installed personal engineering harness.
Do not edit files, run commands, ask the real user a question, or perform the task.
For the quoted task, decide only the immediate next action and which installed skills apply.
Use action ask, plan, implement, stop, or report. Return only the required JSON object.

TASK:
{case['prompt']}
"""


def _json_candidates(value):
    if isinstance(value, dict):
        if {"action", "skills", "reason"} <= value.keys():
            yield value
        for child in value.values():
            yield from _json_candidates(child)
    elif isinstance(value, list):
        for child in value:
            yield from _json_candidates(child)
    elif isinstance(value, str):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            return
        yield from _json_candidates(parsed)


def extract_decision(stdout: str) -> dict:
    candidates: list[dict] = []
    try:
        candidates.extend(_json_candidates(json.loads(stdout)))
    except json.JSONDecodeError:
        for line in stdout.splitlines():
            try:
                candidates.extend(_json_candidates(json.loads(line)))
            except json.JSONDecodeError:
                continue
    if not candidates:
        raise ValueError("provider output contained no structured decision")
    return candidates[-1]


def run_case(provider: str, case: dict, workdir: Path, schema: Path, timeout: int) -> dict:
    command = build_command(provider, workdir, schema)
    started = time.monotonic()
    result = subprocess.run(
        command,
        input=decision_prompt(case),
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    record = {
        "provider": provider,
        "case_id": case["id"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "duration_seconds": round(time.monotonic() - started, 3),
        "exit_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }
    try:
        record["decision"] = extract_decision(result.stdout)
        record["score"] = score_decision(case, record["decision"])
    except ValueError as exc:
        record["score"] = {"passed": False, "failures": [str(exc)]}
    return record


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", choices=["codex", "claude"], required=True)
    parser.add_argument("--suite", default="routing")
    parser.add_argument("--case")
    parser.add_argument("--trials", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--output", type=Path, default=root / "evals/artifacts")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    cases = load_cases(root / "evals", args.suite)
    if args.case:
        cases = [case for case in cases if case["id"] == args.case]
    if not cases:
        parser.error("no matching evaluation cases")
    if args.trials < 1:
        parser.error("--trials must be positive")
    if args.dry_run:
        print(f"Prepared {len(cases)} {args.suite} cases for {args.provider} x {args.trials} trial(s).")
        return 0

    args.output.mkdir(parents=True, exist_ok=True)
    records = []
    for case in cases:
        for _ in range(args.trials):
            records.append(
                run_case(args.provider, case, root, root / "evals/decision.schema.json", args.timeout)
            )
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output = args.output / f"{args.provider}-{args.suite}-{stamp}.json"
    output.write_text(json.dumps(records, indent=2) + "\n")
    passed = sum(record["score"]["passed"] for record in records)
    print(f"{passed}/{len(records)} trials passed; report: {output}")
    return 0 if passed == len(records) else 1


if __name__ == "__main__":
    raise SystemExit(main())
