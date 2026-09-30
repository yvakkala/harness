# Harness Gap Analysis

**Reviewed:** 2026-09-30

The first harness version had a compact core and appropriately narrow skills. Its main gaps were operational: it did not prove that each runtime loaded the instructions, execute behavioral evaluations, manage installation as a complete lifecycle, or enforce its own durable-project checks in CI.

## Findings addressed in 0.2.0

- Claude Code `2.1.181` on the development machine predates native `AGENTS.md` support. Anthropic added fallback support in `2.1.277`; loading both formats requires the `claude-md-and-agents-md` built-in mode. See the [Claude Code release notes](https://github.com/anthropics/claude-code/releases) and [agents-md documentation](https://github.com/anthropics/claude-code/blob/main/mods/agents-md/README.md).
- The original cases were a manual rubric. OpenAI recommends explicit, implicit, contextual, and negative routing tests with trace-based deterministic grading. See [Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills).
- Agent evaluations need trials, trace evidence, and resulting-state checks rather than final-answer claims alone. See [Anthropic's agent evaluation guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).
- Live repository symlinks made unreviewed skill edits active immediately. Versioned managed copies and integrity hashes now separate source editing from installation.
- The durable harness lacked CI, versioning, and traceability. The repository now validates tests, manifests, requirement groups, evaluation suites, and source structure on every proposed change.
- Infrastructure and CI changes were high-impact recurring domains without focused conditional guidance, so two narrow skills were added.

## Deliberately deferred

- Performance and broader data-lifecycle skills remain deferred until evaluation or real usage shows repeated omissions.
- Technology-specific framework and cloud skills remain project-local.
- Live model evaluations are manual or scheduled because they consume model budget and vary across trials. Deterministic repository checks remain the pull-request gate.
- A repository-wide reuse license remains an owner decision. The adapted Superpowers material retains its bundled MIT license.

OpenAI's current guidance warns that large catalogs, long descriptions, and elaborate recipes can reduce routing quality. The catalog therefore grows only for repeated failures, high-impact risks, or explicit preferences. See [Rethinking skills and prompts](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra).
