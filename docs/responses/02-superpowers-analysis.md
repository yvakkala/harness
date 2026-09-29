# Superpowers Analysis and Lessons

Yes. Superpowers is trying to solve the same problem: make good engineering behavior persistent. Its mistake is enforcing an entire development methodology through prompts.

My assessment is that Superpowers has become poorly calibrated rather than simply “bad.”

## What went wrong

The current bootstrap says that if there is even a 1% chance a skill applies, the agent must invoke it. It explicitly treats “this skill is overkill” as invalid reasoning. [See `using-superpowers`](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/using-superpowers/SKILL.md).

That combines with brainstorming rules that:

- Apply before almost any behavior change.
- Require approval before implementing even bounded changes.
- Choose the heavier process whenever uncertain.
- Allow escalation to a heavier process, but no downgrade.
- Require one question per message.
- Route architectural work through spec, plan, execution and review stages.

These are intentional requirements in the [current brainstorming skill](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/brainstorming/SKILL.md).

Each rule sounds defensible by itself. Together they produce this:

```text
request
  → classify
  → questions
  → design
  → approval
  → spec
  → approval
  → plan
  → approval
  → worktree
  → TDD
  → subagent per task
  → task reviews
  → final review
  → branch-finishing workflow
```

That is appropriate for a large, ambiguous, high-risk project. It is painful for “add log rotation,” “fix this validation,” or “rename this endpoint.”

I compared the October 2025 v3.1.0 release with the current v6.4.2 checkout:

| Core workflow skill | v3.1.0 | v6.4.2 |
|---|---:|---:|
| Brainstorming | 156 lines | 285 lines |
| Writing plans | 116 | 204 |
| Executing plans | 76 | 373 |
| Subagent development | 189 | 568 |
| Combined | 537 | 1,430 |

Interestingly, the whole skill collection became slightly smaller. The growth is concentrated in orchestration—the part agents repeatedly load and follow.

The release notes show why. Real failures caused the project to add ledgers, review packages, circuit breakers, model selection rules, approval boundaries, recovery behavior and cross-platform mappings. The maintainers are aware of the cost and recently introduced scaled brainstorming, cheaper inline execution and leaner plans. But even the “bounded” path still stops for approval, and the global mandatory-skill rule remains. [Superpowers release notes](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/RELEASE-NOTES.md)

## Why it felt better in the past

Earlier models benefited more from explicit procedural scaffolding. They were likelier to start coding prematurely, skip testing, lose requirements and forget their place during longer work.

Current frontier agents already have stronger planning, repository exploration, task tracking, testing behavior, context compaction and sometimes native subagents. OpenAI’s recent guidance explicitly says that more capable models need less handholding, that broadly triggered skills can conflict, and that loading unnecessary instructions consumes context and makes skill selection worse. [OpenAI’s current skill guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)

So Superpowers increasingly duplicates behavior the agent already has while overriding its ability to judge how much process a task deserves.

There is also an evaluation mismatch. Superpowers appears heavily optimized for:

- Following the prescribed workflow.
- Resisting shortcuts.
- Passing planted-defect tests.
- Preserving state across long autonomous sessions.

Those are useful measurements, but they do not fully measure:

- Time until useful code.
- Number of human interruptions.
- Token and tool-call cost.
- Unnecessary files and commits.
- Diff size.
- Whether the process was proportionate to the task.

Reddit feedback reflects this. Users report excessive questions, forced worktrees and commits, lost velocity and overly granular plans. Others report much higher quality, especially for large features. That mixed result suggests Superpowers is useful for a narrower class of tasks than its automatic triggers imply. [Discussion about overengineering and control](https://www.reddit.com/r/ClaudeCode/comments/1rmi6pr/anyone_else_not_a_fan_of_the_superpowers_plugin/), [discussion about reduced velocity](https://www.reddit.com/r/ClaudeCode/comments/1slmwt3/has_anyone_noticed_a_drop_in_velocity_using_the/)

## A better design

I would build a much thinner system around outcomes and risk.

| Task | Default process |
|---|---|
| Small and reversible | Inspect, implement, run focused checks |
| Medium behavioral change | Brief plan, tests, implementation, self-review |
| Large or ambiguous feature | Written spec, implementation plan, staged execution |
| High-risk or irreversible | Explicit review and approval gates |

The agent should be allowed to move both up and down this scale as it learns more.

The global instructions can be approximately 30 lines:

```md
Choose process in proportion to risk and ambiguity.

For small, reversible changes:
- Inspect the relevant code.
- Implement directly.
- Run focused verification.
- Do not create plans, worktrees, commits, or subagents unless useful.

For behavioral changes and bug fixes:
- Add or update a meaningful test when practical.
- Verify the test would fail without the fix.
- Run the relevant project checks.

Use a written plan when:
- multiple components or public interfaces change;
- requirements are materially ambiguous;
- migration, security, deployment, or data-loss risk exists;
- work is likely to span several independent tasks.

Ask the user only when the missing answer would materially change the result.
Do not create commits, branches, or worktrees unless requested or already
established by the repository workflow.

Before finishing:
- verify the requested acceptance criteria;
- run relevant tests, lint and type checks;
- report evidence and remaining limitations.
```

Then create narrow domain skills. For example, the logging skill should trigger on:

> “Adding or reviewing production log configuration, rotation or retention. Do not use for adding individual log statements.”

Its body should primarily be an acceptance checklist:

```text
[ ] destination chosen appropriately for deployment
[ ] structured output configured
[ ] max file size configured
[ ] retention period or retained-file count configured
[ ] rotation behavior configured
[ ] log level configured
[ ] timestamps and timezone defined
[ ] secrets are redacted
[ ] invalid values fail during startup
[ ] configuration documented
[ ] tests or deterministic validation added
```

Most critically, those requirements should also exist in a shared logging component, tests or a configuration validator. The skill guides the implementation; CI prevents omissions.

I would retain only the strongest ideas from Superpowers:

- Systematic debugging for difficult bugs.
- Verification before completion.
- TDD for testable behavior.
- Written specifications for genuinely large work.
- Parallel agents for substantial independent tasks.

I would remove:

- The “1% chance means mandatory” bootstrap.
- Brainstorming before every change.
- One-way escalation.
- Mandatory approval for reversible implementation.
- Automatic worktrees and commits.
- Per-task subagent plus per-task reviewer as the default.
- Long arguments designed to stop the model from adapting the workflow.

That gives you persistent standards without turning every request into a miniature enterprise delivery process. The durable guarantees come from templates, configuration schemas, tests and CI; the agent instructions remain a small routing layer.

