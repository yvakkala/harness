# Adaptive Software Engineering Framework — Requirements

**Status:** Draft 0.1  
**Purpose:** Define what a reusable, vendor-independent software-engineering framework for coding agents must accomplish.  
**Scope rule:** This document specifies required outcomes and behavior. It intentionally does not prescribe architecture, file layouts, tools, programming languages, agent prompts, or implementation mechanisms.

## 1. Background

Developers repeatedly communicate the same expectations to coding agents across projects: write maintainable code, use tests appropriately, preserve Git history, configure CI/CD, add production-ready logging, verify work, and avoid unsafe changes. Informal prompts do not reliably preserve all requirements. For example, an agent may configure log retention in one session but omit maximum file size, then reverse the omission in another session.

Existing methodology frameworks attempt to solve this through mandatory planning, questioning, test-driven development, worktrees, commits, subagents, and review stages. This can improve discipline on large tasks, but it also creates excessive ceremony, token consumption, interruptions, and loss of agent judgment on small or well-specified work.

The required framework must make engineering expectations persistent and verifiable while adapting the amount of process to the task, project, and risk.

## 2. Product objective

The framework shall help coding agents produce software that:

1. Solves the intended user or business problem.
2. Satisfies explicit and applicable implied requirements.
3. Exhibits the quality characteristics appropriate to its context.
4. Can be changed, delivered, operated, and retired safely.
5. Provides evidence that its requirements have been met.
6. Avoids process whose cost is disproportionate to the task.

## 3. Goals

### G-1 — Persistent expectations

Users shall be able to state recurring engineering expectations once and have them apply consistently across appropriate future projects and sessions.

### G-2 — Project-specific adaptation

Each project shall be able to define requirements, constraints, commands, risks, and quality targets that refine or override personal defaults.

### G-3 — Requirement completeness

The framework shall reduce omission of explicit and recurring requirements, including multi-part requirements such as logging rotation, maximum file size, and retention.

### G-4 — Proportionate process

The framework shall apply process according to task ambiguity, scope, reversibility, impact, and risk.

### G-5 — Verifiable completion

Completion claims shall be supported by current evidence appropriate to the change.

### G-6 — Sustainable software quality

The framework shall address product value, product quality, delivery quality, operational quality, and maintainability over the software lifecycle.

### G-7 — Portability

Core requirements shall remain usable across coding-agent products and software technology stacks.

## 4. Non-goals

The framework is not required to:

1. Impose one software-development methodology on every task.
2. Maximize every quality attribute for every project.
3. Require specifications, plans, branches, worktrees, commits, subagents, or user approvals for every change.
4. Replace project tests, continuous integration, code review, security controls, or operational monitoring.
5. Make product, architecture, or risk decisions that require missing business context.
6. Guarantee defect-free software.
7. Prescribe a particular programming language, hosting platform, repository provider, or CI/CD service.

## 5. Definitions

- **Personal default:** A recurring preference or standard intended to apply across projects.
- **Project requirement:** A rule, constraint, command, convention, or quality target specific to a repository or product.
- **Domain requirement:** A reusable set of requirements for a recognizable concern such as logging, authentication, database migrations, APIs, or accessibility.
- **Quality profile:** The project-specific selection and prioritization of quality attributes, risks, targets, and required evidence.
- **Mandatory control:** A requirement that cannot be skipped without explicit authority because omission would create unacceptable correctness, security, safety, data, compliance, or operational risk.
- **Evidence:** A current, inspectable result demonstrating that a requirement or acceptance criterion is satisfied.
- **Small task:** A bounded, reversible change with limited impact and sufficient existing context.
- **High-risk task:** A change with significant security, privacy, safety, financial, data-loss, compatibility, regulatory, or production impact.

## 6. Stakeholder requirements

### SR-1 — Developer

The developer needs consistent engineering behavior without repeating the same instructions in every prompt or project.

### SR-2 — Maintainer

The maintainer needs changes that respect project conventions, remain understandable, and include sufficient verification and documentation.

### SR-3 — Reviewer

The reviewer needs traceability from requested behavior to changed artifacts and verification evidence.

### SR-4 — Operator

The operator needs deployable, observable, supportable, recoverable software with documented operational expectations.

### SR-5 — End user

The end user needs software that is correct, usable, reliable, secure, inclusive, and fit for its intended context.

### SR-6 — Organization

The organization needs software delivery that balances value, speed, stability, risk, cost, compliance, and long-term sustainability.

## 7. Instruction and requirement management

### IR-1 — Reusable personal defaults

The framework shall allow a user to define recurring engineering expectations once for reuse across projects.

### IR-2 — Project authority

The framework shall allow projects to define more specific requirements and shall apply those requirements within their stated scope.

### IR-3 — Precedence clarity

When requirements conflict, the framework shall determine precedence consistently and make material conflicts visible.

### IR-4 — Direct user authority

Explicit instructions for the current task shall take precedence over reusable preferences unless doing so would violate a higher-authority constraint or an applicable safety boundary.

### IR-5 — Requirement traceability

For non-trivial work, the framework shall retain a traceable relationship among the request, applicable requirements, acceptance criteria, changes, and verification evidence.

### IR-6 — Requirement freshness

Users shall be able to identify and revise stale, redundant, contradictory, or no-longer-useful requirements.

### IR-7 — Scoped applicability

Requirements shall state when they apply and, where ambiguity is likely, when they do not apply.

### IR-8 — Minimal relevant context

The framework shall avoid burdening a task with unrelated requirements or workflows.

## 8. Adaptive workflow requirements

### AW-1 — Risk-based calibration

The framework shall calibrate its workflow using at least task scope, ambiguity, reversibility, affected users, data sensitivity, production impact, security impact, safety impact, and compliance impact.

### AW-2 — Bidirectional adjustment

The framework shall be able to increase or decrease process when evidence shows that the original assessment was too light or too heavy.

### AW-3 — Small-task autonomy

When a task is sufficiently specified, bounded, reversible, and low risk, the framework shall permit direct implementation and focused verification without mandatory planning artifacts or user checkpoints.

### AW-4 — Complex-task structure

When a task is ambiguous, cross-cutting, long-running, or high risk, the framework shall require enough durable specification and review to manage the identified risks.

### AW-5 — Clarification threshold

The framework shall ask the user a question only when the missing answer would materially change the result, scope, risk, or external effect and cannot be resolved safely from available context.

### AW-6 — No repeated authorization

The framework shall not ask the user to reconfirm work already authorized by the current request or established project workflow.

### AW-7 — No incidental workflow activation

A domain or process workflow shall not activate merely because the task mentions a related technology or concept.

### AW-8 — User workflow control

The user shall be able to request, skip, strengthen, or replace a non-mandatory workflow for the current task.

### AW-9 — Mandatory-control explanation

When a mandatory control blocks or pauses work, the framework shall identify the control, its source, and why it applies.

### AW-10 — No unauthorized repository operations

The framework shall not create commits, branches, worktrees, pushes, pull requests, merges, or history rewrites unless authorized by the user or explicitly required by an established project workflow.

## 9. Software quality requirements

Each project shall evaluate the following quality characteristics for applicability. Applicable characteristics shall have project-appropriate expectations or measurable targets. A characteristic may be marked inapplicable only with a context-based reason.

### QR-1 — Functional suitability

The software shall provide the behavior necessary to satisfy the intended user objectives and acceptance criteria completely, correctly, and appropriately.

### QR-2 — Performance efficiency

The software shall satisfy applicable response-time, throughput, capacity, resource-use, and cost-efficiency expectations under stated conditions.

### QR-3 — Compatibility

The software shall coexist and interoperate with required systems, protocols, data formats, and supported versions.

### QR-4 — Interaction capability

User-facing software shall be understandable, learnable, operable, inclusive, self-describing, and resistant to preventable user error.

### QR-5 — Reliability

The software shall satisfy applicable expectations for correctness over time, availability, fault tolerance, graceful degradation, and recovery.

### QR-6 — Security

The software shall protect confidentiality, integrity, authenticity, accountability, and availability in proportion to its threats and data sensitivity.

### QR-7 — Maintainability

The software shall remain understandable, analyzable, modular, testable, and economical to modify.

### QR-8 — Flexibility

The software shall satisfy applicable expectations for configuration, adaptation, scaling, installation, migration, and replacement.

### QR-9 — Safety

Where software can cause physical, financial, environmental, legal, or substantial social harm, it shall identify applicable hazards, constrain unsafe operation, warn appropriately, and fail safely.

### QR-10 — Accessibility

User-facing software shall meet the accessibility target selected for the project and shall not knowingly exclude supported users.

### QR-11 — Privacy

Software that handles personal or sensitive data shall limit collection, access, exposure, retention, and secondary use according to applicable requirements.

### QR-12 — Economic fitness

Quality targets and controls shall be proportionate to product value, lifecycle, expected usage, risk, and maintenance capacity.

## 10. Lifecycle coverage requirements

### LC-1 — Product intent

The framework shall support identification of intended users, the problem being solved, desired outcomes, constraints, scope, and success measures.

### LC-2 — Requirements

The framework shall support functional requirements, quality requirements, constraints, acceptance criteria, prioritization, and change impact.

### LC-3 — Architecture and design

The framework shall require architectural and design decisions to address the risks and quality attributes material to the task or project.

### LC-4 — Construction

The framework shall require implementation to follow applicable project conventions and to handle inputs, configuration, errors, dependencies, and resources appropriately.

### LC-5 — Data lifecycle

Where data is present, the framework shall account for schema, validation, integrity, migration, access, retention, backup, restoration, and deletion requirements as applicable.

### LC-6 — Verification

The framework shall require verification that is proportionate to the changed behavior and risk, and shall distinguish meaningful tests from tests that merely mirror implementation.

### LC-7 — Secure development

The framework shall incorporate applicable security requirements throughout requirements, design, implementation, verification, release, maintenance, and vulnerability response.

### LC-8 — Build and release

Production software shall have defined expectations for build integrity, automated checks, release readiness, deployment safety, compatibility, and rollback.

### LC-9 — Operations

Operated software shall have applicable expectations for configuration, observability, service levels, alerting, capacity, support, incident response, and operational documentation.

### LC-10 — Continuity and recovery

Where service or data continuity matters, recovery objectives, backup expectations, failover behavior, and restoration evidence shall be defined.

### LC-11 — Documentation

Software shall include documentation appropriate to its users, maintainers, integrators, reviewers, and operators.

### LC-12 — Maintenance and evolution

The framework shall account for ownership, supported versions, compatibility, deprecation, dependency updates, technical debt, and end-of-life expectations as applicable.

### LC-13 — Feedback and improvement

The framework shall support learning from user feedback, production behavior, defects, incidents, reviews, and delivery outcomes.

## 11. Testing and verification requirements

### TV-1 — Acceptance coverage

Every explicit acceptance criterion shall be implemented, verified, or reported as unresolved.

### TV-2 — Requirement-to-evidence mapping

For changes with multiple requirements, the completion report shall make it possible to determine the evidence for each requirement.

### TV-3 — Behavioral testing

Behavioral changes and bug fixes shall include meaningful automated tests when such tests are practical and valuable.

### TV-4 — Test-first policy

When the applicable project or task policy requires test-first development, the framework shall preserve observable evidence that the test failed for the expected reason before the production change and passed afterward.

### TV-5 — Test integrity

The framework shall not weaken, remove, or bypass a valid check solely to obtain a passing result.

### TV-6 — Focused and broader verification

The framework shall run focused verification during development and the broader relevant checks before completion when justified by the change.

### TV-7 — Risk-specific verification

Applicable projects shall add verification for performance, load, concurrency, compatibility, accessibility, security, migration, recovery, or safety when those risks are material.

### TV-8 — Current evidence

Success claims shall rely on current verification results rather than assumptions, previous runs, or unverified agent statements.

### TV-9 — Honest limitations

Any relevant check that could not be performed shall be identified with its practical consequence.

## 12. Git and change-management requirements

### GC-1 — Existing-work preservation

The framework shall detect and preserve unrelated existing changes.

### GC-2 — Destructive-operation protection

The framework shall not discard, overwrite, force-delete, or rewrite user work without explicit authorization for the exact operation and target.

### GC-3 — Reviewable scope

Changes shall remain limited to the requested outcome and necessary supporting work.

### GC-4 — Change coherence

When commits are authorized, each commit shall represent a coherent and reviewable change.

### GC-5 — External publication control

The framework shall not publish code, create or merge reviews, deploy software, or send messages to third parties without authority for that action.

## 13. CI/CD and delivery requirements

### CD-1 — Automated quality gates

Production projects shall define automated checks appropriate to their language, architecture, risk, and deployment model.

### CD-2 — Reproducibility

Build and verification outcomes shall be reproducible enough to support review, release, and incident investigation.

### CD-3 — Protected delivery

Release workflows shall prevent known failing or unverified changes from being presented as release-ready.

### CD-4 — Deployment safety

Production changes shall have deployment and recovery expectations proportionate to their potential impact.

### CD-5 — Configuration validation

Invalid or unsafe production configuration shall be detected before it causes avoidable runtime failure where practical.

### CD-6 — Delivery measurement

Teams shall be able to evaluate delivery throughput and instability using context-appropriate measures.

## 14. Operational requirements

### OP-1 — User-centered service objectives

Operated services shall identify the small set of correctness, availability, latency, durability, throughput, or other indicators that reflect material user expectations.

### OP-2 — Observability

Production systems shall expose sufficient evidence to determine health, investigate failures, and evaluate service objectives.

### OP-3 — Actionable alerting

Alerts shall correspond to conditions requiring timely human or automated action and shall provide enough context to begin response.

### OP-4 — Incident response

Systems with material production impact shall have defined ownership, escalation, mitigation, communication, and recovery expectations.

### OP-5 — Learning from failure

Material incidents and escaped defects shall result in corrective actions that address contributing system or process causes.

### OP-6 — Recovery evidence

Backup, rollback, failover, or restoration capability shall not be considered reliable solely because it is configured; applicable projects shall obtain evidence that recovery works.

## 15. Domain requirement behavior

### DR-1 — Recognizable goal

Each reusable domain requirement set shall correspond to a recognizable engineering goal.

### DR-2 — Precise activation

Each domain requirement set shall define conditions for applicability and significant exclusions.

### DR-3 — Outcome orientation

Domain requirements shall state required outcomes, constraints, and evidence without imposing unrelated lifecycle ceremony.

### DR-4 — Completeness checks

Where a domain contains commonly forgotten paired or grouped requirements, the framework shall evaluate the group as a whole.

### DR-5 — Conditional depth

Domain requirements shall distinguish universal concerns from concerns that depend on deployment model, risk, scale, or product type.

## 16. Production logging requirements

The initial reference domain is production logging because it demonstrates the recurring omission problem.

### LOG-1 — Destination suitability

The logging behavior shall be suitable for the project’s runtime and operational environment.

### LOG-2 — Structured records

Production logs shall use a consistently parseable structure when machine processing is expected.

### LOG-3 — Severity

Log severity levels shall have defined meanings and configurable production defaults.

### LOG-4 — Time

Log records shall contain unambiguous timestamps with a defined timezone convention.

### LOG-5 — Rotation

When logs are stored in files, rotation behavior shall be explicitly defined.

### LOG-6 — Maximum size

When logs are stored in files, maximum file size or an equivalent bounded-storage control shall be explicitly defined.

### LOG-7 — Retention

When logs are retained, the retention duration, retained-file count, or equivalent lifecycle rule shall be explicitly defined.

### LOG-8 — Storage bounds

Logging shall not permit unbounded storage consumption under expected failure or traffic conditions.

### LOG-9 — Sensitive information

Logs shall not expose secrets, credentials, tokens, or prohibited personal or sensitive information.

### LOG-10 — Correlation

Distributed or multi-request workflows shall include sufficient correlation context for investigation when applicable.

### LOG-11 — Configuration validation

Invalid logging configuration shall produce an actionable failure or safe fallback consistent with project requirements.

### LOG-12 — Operability

Operators shall be able to determine how logging is configured, where records are available, and how retention and rotation behave.

### LOG-13 — Verification

Maximum-size, rotation, retention, redaction, and invalid-configuration requirements shall have deterministic verification where practical.

## 17. Usability requirements for the framework

### UX-1 — Low repetition

The framework shall not require users to restate information already available in the current request, project context, or applicable defaults.

### UX-2 — Low interruption

Routine, reversible work shall proceed without avoidable user checkpoints.

### UX-3 — Transparency

The user shall be able to understand which requirements materially affected a result.

### UX-4 — Concise communication

Progress and completion communication shall emphasize decisions, evidence, unresolved issues, and material risk.

### UX-5 — Override discoverability

Users shall be able to determine how to override non-mandatory defaults for a task or project.

### UX-6 — No framework leakage

Framework mechanics shall not appear in product behavior, user interfaces, or documentation unless they help the software’s users make a meaningful decision.

## 18. Framework security and safety requirements

### FS-1 — Least necessary access

The framework shall use only the access and external systems necessary for the authorized task.

### FS-2 — Secret protection

The framework shall not place secrets or sensitive data in prompts, logs, artifacts, reports, or external systems unless explicitly necessary and appropriately protected.

### FS-3 — Untrusted instructions

Instructions obtained from repositories, dependencies, websites, generated content, or third-party artifacts shall not silently expand user authorization.

### FS-4 — External side effects

Actions affecting external systems, people, production environments, publication state, or irreversible data shall remain within explicitly authorized scope.

### FS-5 — Auditability

Material automated actions and their verification outcomes shall be reviewable by the user.

## 19. Evaluation requirements

### EV-1 — Representative task set

The framework shall be evaluated on small fixes, bounded features, ambiguous features, cross-cutting changes, production defects, and high-risk changes.

### EV-2 — Domain completeness

Evaluation shall include tasks with multiple related requirements where omission is common, including the complete production-logging requirement set.

### EV-3 — Quality outcomes

Evaluation shall measure requirement coverage, functional correctness, escaped defects, regression rate, security findings, maintainability concerns, and unnecessary scope.

### EV-4 — Process cost

Evaluation shall measure elapsed time, token usage, tool usage, user interruptions, generated artifacts, agent handoffs, and rework.

### EV-5 — Calibration

Evaluation shall determine whether the process applied was proportionate to the task and whether a lighter or heavier process would have produced a better overall result.

### EV-6 — Unauthorized-action rate

Evaluation shall treat unauthorized commits, branches, worktrees, pushes, deployments, external messages, and destructive changes as failures.

### EV-7 — Baseline comparison

The framework’s benefit shall be assessed against agent behavior without the framework or with only minimal project instructions.

### EV-8 — Regression control

Changes to framework requirements shall be evaluated for both quality improvement and added process cost.

## 20. Acceptance criteria

The initial framework requirements are satisfied when all of the following are demonstrated:

1. A user can define recurring engineering expectations once and apply them across more than one project and supported coding agent.
2. A project can refine those expectations with its own quality profile, commands, risks, and acceptance requirements.
3. A well-specified small change can proceed without mandatory specification, planning document, worktree, commit, subagent, or repeated approval.
4. A complex or high-risk change receives stronger specification, verification, and review appropriate to the identified risk.
5. The framework does not activate an unrelated domain workflow based only on incidental terminology.
6. For a production file-logging task, the framework identifies and verifies rotation, maximum size, retention, bounded storage, timestamps, severity, sensitive-data protection, configuration validity, documentation, and applicable correlation requirements.
7. Every explicit task requirement is either mapped to current evidence or reported as unresolved before completion is claimed.
8. Existing unrelated repository changes remain intact.
9. No repository publication, deployment, destructive action, or external communication occurs without authority.
10. The framework evaluates applicable product qualities across functional suitability, performance efficiency, compatibility, interaction capability, reliability, security, maintainability, flexibility, safety, accessibility, privacy, and economic fitness.
11. Production-service work accounts for delivery, configuration, observability, service objectives, incident response, and recovery where applicable.
12. Evaluation demonstrates improved multi-requirement completeness without imposing the heavyweight workflow on routine low-risk tasks.

## 21. Research basis

These requirements synthesize the following primary standards, bodies of knowledge, operational guidance, and examined framework behavior:

1. [ISO/IEC 25010:2023 product quality model](https://www.iso.org/standard/78176.html) — product-quality characteristics and their use in requirements, acceptance, measurement, and evaluation.
2. [IEEE SWEBOK Guide v4](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf) — software-engineering lifecycle and knowledge areas, including requirements, architecture, design, construction, testing, maintenance, security, quality, and operations.
3. [NIST Secure Software Development Framework](https://www.nist.gov/publications/secure-software-development-framework-ssdf-version-11-recommendations-mitigating-risk) — secure-development practices across the software lifecycle.
4. [OWASP Application Security Verification Standard](https://owasp.org/projects/asvs) — verifiable application-security requirements.
5. [W3C Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/) — accessibility expectations for user-facing web software.
6. [Google SRE guidance on service-level objectives](https://sre.google/sre-book/service-level-objectives/) — user-centered reliability indicators and measurable service objectives.
7. [DORA software-delivery performance metrics](https://dora.dev/guides/dora-metrics/) — delivery throughput and instability outcomes.
8. [Superpowers framework](https://github.com/obra/superpowers) and its [release history](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/RELEASE-NOTES.md) — observed benefits and failure modes of mandatory agent workflows.
9. [OpenAI guidance on skills and prompt scope](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) — precise activation, progressive disclosure, and avoiding unnecessary scaffolding.

## 22. Open requirements questions

The following decisions remain intentionally unresolved and require future product direction:

1. Which coding-agent products must be supported in the first release beyond Codex and Claude?
2. What categories of project criticality will be standardized?
3. Which requirements are universal defaults, and which require explicit project activation?
4. What quantitative overhead thresholds define acceptable performance for small, medium, and large tasks?
5. Which domain requirement sets must accompany production logging in the first release?
6. Which regulated or safety-critical domains, if any, are first-release targets?
7. What evidence-retention and privacy expectations apply to agent transcripts and verification results?
