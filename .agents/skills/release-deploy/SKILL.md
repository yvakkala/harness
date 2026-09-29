---
name: release-deploy
description: Prepare, authorize, execute, or verify a durable release or deployment, including production promotion, migrations, rollback, release notes, and post-deployment health. Do not invoke for an ordinary local commit with no release action.
---

# Release and Deploy

Deliver a traceable artifact safely and verify the resulting environment.

## Authorization boundary

- Disclose before approval when commit, push, merge, or another action will deploy automatically.
- A routine reversible deployment explicitly included in an approved plan or direct instruction needs no second approval.
- Available credentials do not imply permission to deploy.
- A high-risk or effectively irreversible production release requires final approval after the exact artifact, migrations, checks, recovery plan, and risks are reviewable.
- A failed required check or material scope change invalidates the affected authorization.

## Release workflow

1. Identify the target environment, release source, automatic triggers, dependencies, migrations, user impact, and recovery path.
2. Read [the release gates](references/gates.md) and apply the gates relevant to the system's risk.
3. Build once and promote the same immutable artifact. Keep environment configuration outside it and trace the release to source, dependencies, build, and CI result.
4. Prevent concurrent incompatible deployments. Use health checks and a rollout strategy suited to availability requirements.
5. Stop, roll back, or begin the established forward-recovery path when health fails.
6. Inspect resulting external state and critical behavior; do not rely only on a successful deployment command.
7. Record the release identifier, environment, migration, health evidence, and rollback or recovery status.
