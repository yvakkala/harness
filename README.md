# Personal Agent Engineering Harness

This repository turns the approved [personalized requirements](docs/personalized-requirements.md) into compact instructions, focused skills, deterministic validation, and behavioral evaluation cases for coding agents.

## Layout

- `AGENTS.md` contains the small always-active behavioral core used by Codex and Claude.
- `.agents/skills/` contains provider-neutral Agent Skills loaded only for relevant work.
- `docs/skill-sourcing.md` records upstream research, licensing, and adopt/adapt/reject decisions.
- `evals/` contains representative behavior cases and their scoring rubric.
- `scripts/install.py` installs the shared instructions and skills for supported local runtimes.
- `scripts/validate.py` checks structure, references, skill metadata, and context-size constraints.

The detailed requirements document remains the source of truth. It should be consulted by section when evolving this harness, not loaded into every coding session.

## Validate

```bash
python -m unittest discover -s tests -v
python scripts/validate.py
```

## Install

Preview the changes:

```bash
python scripts/install.py --dry-run
```

Install for both supported runtimes:

```bash
python scripts/install.py --target all
```

The installer refuses to replace unmanaged files. Managed files can be refreshed by running the command again. Use `--target codex` or `--target claude` to install only one runtime.

## Project-specific instructions

Copy `templates/project/AGENTS.md` into a project and replace its prompts with verified project facts. Keep personal defaults in this harness and project-specific commands, architecture, constraints, and overrides in the project file.
