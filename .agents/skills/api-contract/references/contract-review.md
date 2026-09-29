# Contract Review Points

Cover only dimensions that apply:

- Resource or operation semantics and ownership.
- Input validation, unknown fields, defaults, limits, and safe error detail.
- Authentication, operation-level authorization, resource-level authorization, and tenant isolation.
- Status, error identifiers, retryability, timeouts, cancellation, rate limits, and idempotency.
- Pagination, filtering, sorting, timestamps, locale-sensitive values, and numeric precision.
- Compatibility across server, web, mobile, extension, CLI, and integration versions.
- Event delivery, ordering, duplication, replay, retention, and schema evolution.
- Webhook authenticity, retry schedule, duplicate handling, and observability.
- Deprecation notice, replacement, consumer migration, support window, and removal condition.
- Correlation and diagnostics without sensitive payload logging.

Verify upgrades from the oldest supported consumer where practical. Keep machine output stable and separate from human diagnostics for CLI contracts.
