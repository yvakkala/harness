# Software Quality Research Synthesis

Yes. Before creating our alternative to Superpowers, we need a defensible model of “good software.” Otherwise we will encode personal habits and accidentally create another bloated methodology.

The research suggests three separate questions:

1. Does the software solve the right problem?
2. Is the software product well built?
3. Can it be changed, delivered and operated sustainably?

ISO/IEC 25010:2023 defines nine product-quality characteristics and recommends using them to define requirements, tests, acceptance criteria and measurements throughout the lifecycle. [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html)

| Product quality | What it means |
|---|---|
| Functional suitability | It provides the correct, complete and appropriate behavior. |
| Performance efficiency | It meets latency, throughput, capacity and resource targets. |
| Compatibility | It coexists and interoperates correctly with other systems. |
| Interaction capability | It is understandable, learnable, operable, inclusive and resistant to user error. |
| Reliability | It remains available, tolerates faults and recovers correctly. |
| Security | It protects confidentiality, integrity, authenticity and accountability. |
| Maintainability | It is understandable, modular, testable and economical to modify. |
| Flexibility | It adapts, scales, installs and can be replaced or migrated. |
| Safety | It identifies hazards, fails safely and avoids harm. |

That model describes the product, but it does not fully describe product value, delivery, operations or the engineering organization. IEEE’s SWEBOK v4 covers 18 knowledge areas, including requirements, architecture, design, construction, testing, maintenance, security, quality, operations, configuration management and engineering management. It explicitly treats development, operation and maintenance as one discipline. [IEEE SWEBOK v4](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)

A practical complete model therefore looks like this:

| Engineering component | What must be decided or produced |
|---|---|
| Product intent | Users, problem, expected outcome, scope and success measures |
| Requirements | Behaviors, constraints, acceptance criteria and traceability |
| Quality profile | Which ISO qualities matter most and their measurable targets |
| Architecture | Boundaries, dependencies, interfaces, data flows and failure modes |
| Implementation | Modular code, validation, error handling, configuration and dependencies |
| Data | Schemas, integrity, migrations, retention, privacy, backup and restoration |
| User experience | Workflows, accessibility, responsiveness and user-error protection |
| Verification | Unit, integration, contract, end-to-end and risk-specific tests |
| Security | Threat model, authentication, authorization, secrets and dependency controls |
| Build and delivery | Reproducible builds, CI, artifacts, environments, deployment and rollback |
| Operations | Telemetry, SLOs, alerting, capacity, runbooks and incident response |
| Resilience | Timeouts, retries, graceful degradation, recovery and disaster testing |
| Documentation | User, developer, API, architectural and operational documentation |
| Evolution | Ownership, versioning, compatibility, deprecation and technical-debt management |
| Governance | Compliance, audit evidence, risk decisions and change control |
| Improvement | User feedback, production data, delivery metrics and postmortem actions |

Security needs its own lifecycle controls. NIST’s SSDF divides this into preparing the organization, protecting software, producing well-secured software and responding to vulnerabilities. OWASP ASVS supplies concrete application-security requirements that can be tested. [NIST SSDF](https://www.nist.gov/publications/secure-software-development-framework-ssdf-version-11-recommendations-mitigating-risk), [OWASP ASVS](https://owasp.org/projects/asvs)

For user-facing web software, accessibility must be an explicit component. WCAG 2.2 organizes it around four properties: perceivable, operable, understandable and robust. [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)

For production systems, observability is insufficient without user-centered objectives. Google’s SRE guidance recommends selecting a small number of indicators based on what users care about—such as correctness, availability, latency and durability—and defining measurable SLOs. [Google SRE on SLOs](https://sre.google/sre-book/service-level-objectives/)

Finally, the engineering process itself should be measured. DORA currently uses five delivery measures: change lead time, deployment frequency, failed-deployment recovery time, change fail rate and deployment rework rate. These measure whether the organization can ship quickly without creating instability. [DORA metrics](https://dora.dev/guides/dora-metrics/)

The central insight is that good software does not maximize every property. A prototype, an internal script, a banking service and a medical device need different levels of reliability, safety, documentation and governance. We need a project-specific **quality profile**.

A repository could express that in `QUALITY.md`:

```md
# Quality profile

## Purpose
Who uses this system and what outcome does it provide?

## Criticality
Prototype | Internal | Production | Business-critical | Safety-critical

## Priority qualities
1. Functional correctness
2. Security
3. Reliability
4. Maintainability

## Measurable targets
- Availability: 99.9%
- API latency: p95 below 300 ms
- Recovery time objective: 2 hours
- Recovery point objective: 24 hours
- Supported environments: ...
- Accessibility target: WCAG 2.2 AA

## Mandatory controls
- CI tests, lint and type checking
- Dependency and secret scanning
- Reviewed database migrations
- Structured logs, metrics and traces
- Tested backup restoration
- Deployment rollback procedure

## Verification
- Focused checks: ...
- Full checks: `make check`
- Operational readiness: `make verify-production`
```

Our agent framework should then work like this:

```text
Global engineering principles
           ↓
Repository quality profile
           ↓
Task requirements and risk
           ↓
Relevant domain skill only
           ↓
Tests, validation and CI evidence
```

This avoids Superpowers’ main failure. We do not force every quality component into every interaction. The project selects applicable qualities once; each skill loads only the relevant guidance; automated controls enforce the requirements that matter.

For example, a logging task would load logging requirements because the project quality profile says it is a production service. It would check retention, maximum size, structured output, redaction and operability. It would not trigger brainstorming, architectural planning, worktrees and subagent reviews unless the actual change justified them.

The framework should consequently contain:

- A concise universal definition of done.
- A project quality-profile template.
- Focused skills for security, logging, APIs, databases, UI accessibility, reliability and delivery.
- Reusable implementation templates.
- Deterministic validation scripts.
- CI workflows.
- A risk-based process router.
- Evaluation cases measuring defects, time, tokens, interruptions and unnecessary code.

That gives us a research-backed foundation without turning every standard into mandatory ceremony.

