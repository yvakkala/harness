# Approved Observability Defaults

Project-specific legal, privacy, contractual, operational, and storage requirements override these values.

## Logs

- Centralized production diagnostic logs: searchable for 90 days.
- Standalone production files: rotate at 100 MiB or 24 hours, whichever occurs first; compress rotated files; retain for 90 days.
- Standalone total cap: 5 GiB per service. Remove the oldest eligible diagnostic logs before storage exhaustion and surface when the cap prevents the 90-day target.
- Security audit records: retain for 90 days unless a different obligation applies.
- Local development: retain 7 days with a 500 MiB cap per project.
- Mobile, desktop, and browser-extension diagnostics: retain 7 days with a 10 MiB local cap per application.

Never sample away errors, required security audit records, or compliance-required events. Elevated production debug logging must expire or be deliberately disabled.

## Metrics and traces

- Full-resolution production metrics: 30 days.
- Aggregated production metrics: 13 months.
- Ordinary sampled traces: 7 days.
- Failed or designated high-value traces: 30 days.

Measure applicable traffic, errors, latency, saturation, queue health, and a small set of critical business outcomes. Do not use unbounded labels such as user IDs, request IDs, raw URLs, or arbitrary error text.

## Alerts

Alert on user-visible failure, service-objective risk, security conditions requiring response, and approaching resource exhaustion. Each alert needs an owner, severity, actionable context, response guidance, and verified delivery path.
