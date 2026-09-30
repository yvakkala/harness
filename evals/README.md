# Behavioral evaluations

`cases.json` is the manual provider-neutral policy suite. `routing.json` contains executable positive and negative routing cases for every installed skill. `tasks.json` defines sandboxed fixture work with deterministic resulting-state checks. `decision.schema.json` defines the structured decision emitted by live routing trials.

## Run an evaluation

1. Run `python scripts/doctor.py` and resolve compatibility or integrity failures.
2. Use `scripts/evaluate.py` for routing cases. It constrains the provider to a read-only or plan decision, saves raw output, and grades action and selected skills.
3. Use `scripts/evaluate_tasks.py` for fixture tasks. It copies the fixture into a temporary workspace, records the provider trace, and grades the resulting filesystem state and changed-file scope.
4. Run manual policy cases in a clean representative repository. Submit each `prompt`, inspect the trace and resulting state, and do not grant permissions beyond the case.
5. Record the provider, model, runtime version, harness commit, date, trial count, pass rate, and evidence note.

A case passes only when every expectation passes. Because model output varies, run at least three trials before a harness or model upgrade. Treat a regression in destructive-action approval, data safety, secret handling, instruction loading, or the two-attempt stop rule as release-blocking. Review other failures before release and either fix them or document why the expectation changed.

Validate the suite structure with:

```bash
python scripts/validate.py
python scripts/evaluate.py --provider codex --dry-run
python scripts/evaluate.py --provider claude --dry-run
python scripts/evaluate_tasks.py --provider codex --dry-run
python scripts/evaluate_tasks.py --provider claude --dry-run
```

Routing trials deliberately test the immediate decision and skill selection rather than allowing arbitrary repository mutation. Add sandbox fixture repositories and deterministic resulting-state graders when a real failure cannot be represented at this layer. These cases do not replace project tests.
