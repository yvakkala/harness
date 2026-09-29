# Durable Project Baseline

Select controls by relevance. Do not generate empty directories or configuration for concerns the project does not have.

## Product and architecture

- Record the intended outcome, primary users or callers, acceptance examples, supported environments, and material constraints.
- Prefer the simplest cohesive architecture that meets current needs. A modular monolith is the default for a new server unless distribution has a demonstrated reason.
- Make boundaries, data ownership, public contracts, and consequential architectural decisions discoverable.

## Developer workflow

- Initialize Git when the project is not already within a repository.
- Provide authoritative install, run, focused-test, full-test, format, lint, type-check, and production-build commands as applicable.
- Commit dependency locks and generated artifacts only when the ecosystem expects them.
- Provide deterministic local setup, using containers only when they reduce real environment friction.

## Verification

- Configure formatting, linting, strong practical type checking, meaningful tests, and production builds appropriate to the stack.
- Give database-backed tests a dedicated isolated test database and protect other environments from test access.
- Add a small reliable end-to-end path only when a critical user journey crosses meaningful boundaries.
- Run required checks in CI for pull requests and the default branch.

## Security and data

- Keep secrets out of source, logs, fixtures, artifacts, and client bundles. Provide placeholder example configuration.
- Validate untrusted boundaries, enforce authorization at trusted services, and apply least privilege.
- Define sensitive-data ownership, access, retention, deletion, and backup requirements before production use.
- Lock dependencies and enable suitable secret, dependency, and source checks.

## Delivery and operations

- Build a traceable release artifact and keep environment-specific configuration outside it.
- Define deployment trigger, health verification, rollback or forward recovery, and any production approval gate.
- Add logging and other observability only where operation requires them; use the `logging-observability` skill for production telemetry.
- Define backups and verified restoration for irreplaceable state.

## User experience and documentation

- Optimize common tasks for direct completion and meet the applicable accessibility target.
- Provide a concise entry document and project `AGENTS.md` containing only verified project facts and overrides.
- Avoid separate documents without a real reader or maintenance value.
