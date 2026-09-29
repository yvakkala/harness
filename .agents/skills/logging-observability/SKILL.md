---
name: logging-observability
description: Implement or change durable application logging, security audit records, metrics, traces, dashboards, alerts, rotation, or telemetry retention. Use for production observability work, not ordinary debugging output or quick experiments unless explicitly requested.
---

# Logging and Observability

Make production behavior diagnosable without exposing sensitive data or allowing telemetry to consume unbounded resources.

## Establish the requirement

Inspect the runtime, hosting model, existing telemetry platform, failure modes, compliance needs, traffic, storage constraints, and repository conventions. Preserve sound existing choices. When the project has no explicit policy, apply [the approved defaults](references/defaults.md).

## Required behavior

- Use structured production events with UTC timestamp, severity, service, environment, release, event name, and correlation context where applicable.
- Record useful lifecycle, operation outcome and duration, error, dependency failure, background-work, and security events. Avoid routine noise.
- Preserve exception causes and safe diagnostic context. Do not log secrets, authenticators, unnecessary personal data, or full request and response bodies by default.
- Use standard streams for container or platform-managed services. Use bounded rotating files only when a reliable collector is unavailable.
- Keep local and CLI output readable without corrupting machine-consumed output.
- Make log level and limits configurable and validate them before accepting production work.
- Keep security audit records separate when their access, integrity, or retention differs.
- Add metrics, tracing, dashboards, and alerts only when they answer an operational question. Bound label cardinality and trace attributes.

## Verification

Test the configuration and behavior that can silently fail: structured fields, severity mapping, correlation propagation, redaction, file rotation, compression, retention, total caps, and alert delivery. Generate enough test data to cross a rotation boundary when file logging is used. Confirm telemetry contains no test secret or payload fixture.

Report the effective destinations, limits, retention, verification performed, and any platform-managed behavior that could not be exercised locally.
