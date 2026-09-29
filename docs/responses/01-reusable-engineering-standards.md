# Reusable Engineering Standards Across Projects

The reliable fix is to stop treating these requirements as things the model must remember. Turn them into versioned instructions, reusable workflows, project templates, and automated checks.

Use four layers:

1. **Global instructions** for your personal engineering habits.
2. **Repository instructions** for project-specific commands and architecture.
3. **Skills** for repeatable workflows such as “implement production logging.”
4. **Tests and CI** to make omissions fail automatically.

For Codex, place personal defaults in:

```text
~/.codex/AGENTS.md
```

For Claude Code, keep equivalent defaults in:

```text
~/.claude/CLAUDE.md
```

A useful global file might contain:

```md
# Engineering defaults

## Changes
- Inspect the repository and existing conventions before editing.
- Preserve unrelated work and avoid destructive Git operations.
- Prefer the smallest complete change that solves the requirement.
- Do not claim completion until relevant verification passes.

## Testing
- For behavioral changes, begin with a failing test when practical.
- Implement the minimum code needed to pass it, then refactor.
- Run focused tests while developing.
- Before finishing, run the relevant test, lint, formatting, and type-check commands.
- Never weaken or delete a valid test merely to make a change pass.

## Git
- Check Git status before making changes.
- Keep changes reviewable and logically grouped.
- Do not commit, push, or rewrite history unless the task authorizes it.

## Delivery
- When adding a new service, include its test, lint, build, and deployment checks in CI.
- Report what changed, what was verified, and any remaining limitation.
```

Keep this file short. Global instructions should contain principles that apply almost everywhere. OpenAI’s guidance similarly recommends keeping `AGENTS.md` current and making references conditional instead of forcing the agent to read a large stack of documents on every task. Codex loads applicable `AGENTS.md` files from global through progressively deeper repository directories, so repositories can override or refine your defaults. [OpenAI guidance on AGENTS.md](https://developers.openai.com/api/docs/guides/latest-model)

Each repository should then have its own `AGENTS.md` and `CLAUDE.md`:

```md
# Project instructions

## Commands
- Unit tests: `make test`
- Full verification: `make check`
- Local development: `make dev`
- Database migrations: `make migrate`

## Architecture
- Domain logic belongs in `src/domain`.
- HTTP handlers must not access the database directly.
- All configuration must be validated during startup.

## Definition of done
A code change is complete only when:
- Relevant tests pass.
- Formatting, linting, and type checking pass.
- User-facing behavior is documented.
- Configuration examples are updated.
- CI covers any newly introduced build or verification step.
```

For logging, create a dedicated reusable skill instead of growing your global file. Skills are designed to package repeatable instructions, supporting references, templates, and scripts; the model loads the full instructions when the task matches the skill or you invoke it explicitly. [OpenAI Skills documentation](https://developers.openai.com/plugins/concepts/skills)

For example:

```text
~/.codex/skills/production-logging/
├── SKILL.md
├── references/
│   └── logging-requirements.md
└── assets/
    └── logging-config.example
```

`SKILL.md`:

```md
---
name: production-logging
description: Implement or review production logging, including rotation, retention, structured output, redaction, and operational verification.
---

When asked to add, configure, migrate, or review application logging:

1. Inspect the language, framework, deployment environment, and existing logging.
2. Establish explicit configuration for:
   - maximum file size;
   - retention period or retained-file count;
   - rotation behavior;
   - log level;
   - structured output format;
   - timestamps and timezone;
   - sensitive-data redaction;
   - environment-variable overrides.
3. Prefer stdout/stderr for container platforms unless the repository requires files.
4. Validate invalid configuration during startup.
5. Add tests or deterministic validation covering size and retention settings.
6. Update configuration examples and operational documentation.
7. Run the repository’s relevant checks.
8. Report each requirement and where it was implemented.
```

Use the same skill content for Claude where its skill installation supports it, or keep the skill in a small `engineering-playbook` Git repository and have a bootstrap script install it for both tools. OpenAI recommends focused skills built around a recognizable goal, with detailed policies and templates in supporting files. [Building reusable skills](https://developers.openai.com/plugins/build/skills)

The most important step is converting requirements into executable checks. A prompt saying “remember retention” is probabilistic. A test that fails when retention is absent is deterministic. For logging, your starter code or shared library should test that:

```text
max_file_size > 0
retention_days > 0
rotation is enabled
production log level is configured
secrets are redacted
invalid values fail during startup
```

Then make CI run one standard command such as:

```bash
make check
```

That command should run tests, linting, formatting checks, type checking, security checks where applicable, and configuration validation. Protect the main branch so CI must pass.

Finally, create a project template rather than configuring every repository manually:

```text
project-template/
├── AGENTS.md
├── CLAUDE.md
├── Makefile
├── .github/workflows/ci.yml
├── .editorconfig
├── logging/
│   ├── config.example
│   └── config_test.*
└── docs/
    └── engineering-standards.md
```

Your workflow then becomes:

```text
Personal preferences → global AGENTS.md / CLAUDE.md
Repeatable task       → skill
Project conventions   → repository instructions
Hard requirements     → code, tests, and CI
New repository        → project template
```

This also gives you a good rule for where information belongs: if forgetting it would break production, encode it in code or CI; if it describes how to perform a recurring task, make it a skill; if it varies by repository, put it in the repository instructions; if it is a general preference, put it in the global file.

