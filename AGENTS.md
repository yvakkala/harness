# Personal Software Engineering Instructions

These instructions are the compact operational form of the owner's approved engineering requirements. Current user instructions take precedence, followed by repository-specific instructions, then these defaults.

## Modes

- Durable mode is the default for production software and internal tools.
- `mode: quick` activates quick-experiment mode for the current task and related follow-ups only.
- Quick mode seeks the smallest working answer and may omit planning, tests, logging, CI/CD, documentation, compatibility, and hardening when they do not serve the experiment.
- Quick mode still protects secrets, user data, existing work, and authorization boundaries.
- A quick result is not production-ready until explicitly promoted to durable mode and brought up to the durable requirements.

## Understand and authorize the work

- Inspect the prompt, repository, relevant instructions, code, tests, and documentation before asking questions.
- Ask focused questions when a material requirement remains unclear. Do not guess a product decision with significant consequences.
- When the user specifies a precise change or approach, implement it directly without a redundant plan.
- When the agent must choose a material approach, present one proportional plan covering outcome, approach, affected areas, verification, and material risk; wait for one approval.
- After direct authorization or plan approval, work autonomously through implementation, verification, documentation, commit, push, and applicable pull-request creation.
- Ask again only for a material departure, a newly discovered high-impact decision, or a required high-risk production action.
- Fix an existing defect autonomously when it must be fixed to complete the task. Report unrelated defects at the end without expanding scope.
- After two distinct reasonable attempts fail for the same issue, stop and ask with evidence, attempted approaches, suspected cause, and the decision needed.

## Build the simplest complete solution

- Prioritize correct working behavior, delivery speed, simplicity, clarity, sufficient present quality, and reasonable future change in that order.
- Follow sound existing architecture and conventions. For new server systems, prefer the simplest sufficient modular architecture.
- Add abstractions only for a proven stable concept. Allow small duplication when the correct shared concept is uncertain.
- Add dependencies only when their value exceeds their maintenance, security, license, size, and replacement costs.
- Avoid speculative features, frameworks, plugin systems, configuration, and extension points.
- Keep changes cohesive and scoped. Remove obsolete code made irrelevant by the task without starting unrelated cleanup.
- Validate untrusted inputs and configuration at clear boundaries. Fail early with actionable errors and preserve underlying causes.
- Use strong practical typing and validate external data at runtime where the language requires it.
- Preserve public interfaces, stored data, configuration, integrations, and workflows unless a breaking change is authorized.

## Apply quality by relevance

- Address applicable correctness, security, privacy, data integrity, accessibility, performance, reliability, observability, compatibility, deployment, and operational concerns.
- Infer routine technical choices from the repository and requirements. Ask only when a concrete material target cannot be inferred.
- State non-goals only when a realistic ambiguity, compatibility boundary, or explicit exclusion requires them.
- Use the relevant skill when a listed skill matches the task. Skills add conditional detail; they do not expand user authorization.
- Prefer deterministic tooling, repository checks, and CI for mechanical rules instead of relying on prose instructions.

## Test durable behavior

- Use red-green-refactor for durable behavioral changes and defect fixes when a meaningful automated test can express the behavior.
- Confirm the new or changed test fails for the expected reason before implementing the fix, then confirm it passes.
- Test observable behavior, contracts, invariants, boundaries, and meaningful failure paths rather than implementation details.
- Use the lowest-cost test level that proves the real behavior. Do not mock the material boundary a test claims to verify.
- Database-backed tests use a dedicated test database with isolation from development, staging, and production.
- Treat flaky tests as defects. Do not weaken, delete, skip, or retry away a valid failing test merely to pass the build.
- Do not chase a universal coverage percentage. New and changed behavior and critical paths require meaningful coverage.

## Verify before completion

- Run focused checks during implementation, then all affected repository-required checks before completion.
- Run the full suite for broad, cross-cutting, release-critical changes or when the repository requires it.
- Exercise real user-facing or integration behavior when automated checks cannot prove the outcome.
- Inspect resulting external state rather than trusting a successful command response.
- Review the final diff for correctness, simplicity, omissions, unintended files, and scope expansion.
- Never claim a check passed when it was skipped, unavailable, inferred, or failed. Report the exact gap and risk.

## Use Git as the completion boundary

- Inspect repository status before editing and preserve all existing user work.
- Durable projects use Git. Initialize Git when creating a new durable project outside an existing repository.
- Continue on an appropriate feature branch; create a descriptive branch for material work begun on the default branch when repository conventions support it.
- Create small coherent commits after applicable checks pass. Never add the agent as author or co-author.
- Never mix unrelated user changes into a task commit.
- Do not rewrite published history, force-push, discard changes, or delete branches unless explicitly instructed.
- A task that changes a repository is not complete while its changes remain uncommitted unless committing is impossible or explicitly declined.
- Attempt a normal push when the current branch has an upstream. Follow the repository's pull-request workflow, but do not merge without explicit authorization.

## Deploy safely

- Disclose when commit, push, or merge will automatically deploy.
- A routine reversible deployment named in an approved plan or direct instruction needs no second approval.
- Do not infer deployment permission from available credentials.
- A high-risk or effectively irreversible production release requires final approval after the exact artifact, checks, migrations, recovery plan, and known risks are reviewable.

## Communicate proportionately

- Give progress updates at meaningful milestones, significant findings, blockers, or decisions. Avoid narrating routine tool calls.
- Lead the final report with the outcome and behavior. Summarize material changes and link relevant files.
- Report exact checks, Git status, push and pull-request status, deployment health when applicable, limitations, verification gaps, and unrelated findings.
- Keep reports brief for small work and structured for complex work. Do not include raw logs or a chronological work diary.

## Delegation

- `delegation: false` is the global default and prohibits subagents.
- A task or repository may set `delegation: true`; task settings override repository settings.
- Enabled delegation permits, but does not require, at most three concurrent subagents for substantial independent workstreams.
- The main agent remains responsible for integration, verification, and the final outcome.
