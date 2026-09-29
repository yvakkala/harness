---
name: database-migration
description: Design, implement, or review durable database schema changes, data migrations, SQL scripts, stored-state transformations, or compatibility-sensitive persistence changes.
---

# Database Migration

Preserve data integrity and supported application behavior throughout deployment and recovery.

## Workflow

1. Inspect the current schema, constraints, data volume, access paths, deployment model, supported versions, backup state, and migration tooling.
2. Define the invariant and resulting data model. Prefer database enforcement for rules that concurrent processes or multiple writers must share.
3. Identify old/new application coexistence, locks, rewrite cost, retry behavior, and failure points. Read [migration safety](references/migration-safety.md) for material changes.
4. Present a plan when the sequence, compatibility strategy, or data transformation requires a material choice. Obtain explicit authorization for destructive or effectively irreversible changes after impact and recovery are concrete.
5. Create migration verification before relying on the implementation: fresh install, upgrade from the oldest supported state, expected failure, and representative data where relevant.
6. Implement the smallest staged change that preserves compatibility. Keep schema changes deterministic, reviewable, and automated.
7. Verify application behavior against a dedicated test database, inspect the resulting schema and data, and validate recovery.

## Constraints

- Never point migration tests at development, staging, or production data.
- Do not claim rollback support unless it has been exercised or the exact forward-recovery path is established.
- Do not combine unrelated schema cleanup with the requested migration.
- Preserve timestamps, time zones, precision, identifiers, nullability, uniqueness, and deletion semantics deliberately.
