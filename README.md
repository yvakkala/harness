# Personal Agent Engineering Harness

This repository turns the approved [personalized requirements](docs/personalized-requirements.md) into compact instructions, focused skills, deterministic validation, and behavioral evaluations for coding agents. The current harness version is recorded in [`VERSION`](VERSION), with material changes in [`CHANGELOG.md`](CHANGELOG.md).

## Layout

- `AGENTS.md` contains the small always-active behavioral core used by Codex and Claude.
- `.agents/skills/` contains provider-neutral Agent Skills loaded only for relevant work.
- `docs/skill-sourcing.md` records upstream research, licensing, and adopt/adapt/reject decisions.
- `evals/` contains representative behavior cases and their scoring rubric.
- `scripts/install.py` transactionally installs managed copies, reports status, and uninstalls them safely.
- `scripts/doctor.py` checks provider compatibility and installed-file integrity.
- `scripts/evaluate.py` executes read-only routing trials through Codex or Claude and saves traces.
- `scripts/validate.py` checks structure, references, skill metadata, provenance, coverage, and evaluations.
- `skills.lock.json` records the provenance and hash of every installed skill file.

The detailed requirements document remains the source of truth. It should be consulted by section when evolving this harness, not loaded into every coding session.

## Validate

```bash
python -m unittest discover -s tests -v
python scripts/validate.py
python scripts/update_manifest.py --check
```

## Install

Preview the changes:

```bash
python scripts/install.py --dry-run
```

Install for both supported runtimes:

```bash
python scripts/install.py --target all --configure-claude-agents
```

The installer validates all requested targets before writing, stages the complete payload, replaces only files matching its prior manifest, removes stale managed skills, and rolls back an interrupted activation. It refuses to replace unmanaged or edited files. Run the same command to refresh managed copies. Use `--target codex` or `--target claude` for one runtime.

Inspect or remove the installation:

```bash
python scripts/install.py --status
python scripts/doctor.py
python scripts/install.py --uninstall --target all
```

Claude Code must be version 2.1.277 or newer for native `AGENTS.md` loading. The `--configure-claude-agents` option preserves other user settings and selects `claude-md-and-agents-md`, ensuring the personal baseline remains active even when a repository contains `CLAUDE.md`. The doctor reports an actionable failure when the runtime or setting is incompatible. See the [provider compatibility matrix](docs/provider-compatibility.md) for discovery paths and limitations.

## Behavioral evaluations

Validate command construction without invoking a model:

```bash
python scripts/evaluate.py --provider codex --dry-run
python scripts/evaluate.py --provider claude --dry-run
```

Run one routing suite or a selected case:

```bash
python scripts/evaluate.py --provider codex --suite routing
python scripts/evaluate.py --provider claude --suite routing --case logging-implicit --trials 3
python scripts/evaluate_tasks.py --provider codex --task precise-logging-retention
```

Routing runs use read-only or plan permissions and deterministically grade the selected action and skills. Fixture tasks copy a known repository into an isolated temporary workspace, permit edits only there, grade resulting files and scope, and retain the trace and resulting workspace under ignored `evals/artifacts/`. Both runners avoid session persistence. Live runs consume provider usage and should be performed manually or on a controlled schedule rather than on every pull request.

## Project-specific instructions

Copy `templates/project/AGENTS.md` into a project and replace its prompts with verified project facts. Keep personal defaults in this harness and project-specific commands, architecture, constraints, and overrides in the project file.

## Maintaining the catalog

After changing any skill, regenerate and verify the provenance manifest:

```bash
python scripts/update_manifest.py
python scripts/validate.py
```

The [coverage map](docs/coverage.json) accounts for each approved requirement group without copying all 621 requirements into active context. The [sourcing record](docs/skill-sourcing.md) explains why each external technique was adopted, adapted, deferred, or rejected.
