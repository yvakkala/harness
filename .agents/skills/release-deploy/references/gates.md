# Release Gates

## Before release

- Required formatting, linting, type checks, tests, security checks, builds, migration checks, and platform checks pass.
- The artifact is uniquely identified and traceable to the reviewed commit and resolved dependencies.
- Secrets and environment configuration are supplied through protected channels.
- Destructive migrations have explicit authorization, a recent recoverable backup, and exercised recovery.
- User-visible breaking changes have migration guidance and applicable deprecation handling.
- Release notes cover user behavior, breaking changes, migrations, and operator actions.

## During release

- Deploy only the approved artifact to the approved environment.
- Prevent deployment races and preserve a record of the acting identity and release inputs.
- Observe health, errors, saturation, migration progress, and critical user behavior at a level proportionate to risk.

## After release

- Verify the resulting version, configuration identity, schema state, health, and a representative critical operation.
- Confirm no material regression in user-visible errors, latency, or resource saturation.
- Tag production releases and update the pull request or release record when the repository uses them.
- If recovery was required, report achieved recovery time and any data loss.
