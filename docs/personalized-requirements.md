# Personalized Software Engineering Requirements

**Status:** Approved  
**Version:** 1.0  
**Approved:** 2026-09-30  
**Owner:** Workspace user  
**Purpose:** Record the owner's reusable software-engineering requirements and preferences for coding agents across projects.  
**Scope rule:** This document defines desired outcomes, constraints, and agent behavior. It does not prescribe implementation architecture or vendor-specific mechanisms.

## How this document is personalized

Each section has been discussed and approved separately. Future undecided topics shall be marked explicitly as unresolved rather than filled with assumed preferences.

Project-specific requirements may strengthen or refine these personal defaults. Direct task instructions may override personal defaults unless an applicable project requirement, safety boundary, or explicitly mandatory control has higher authority.

## 1. Scope and project profiles

**Status:** Approved

### Covered work

These personal requirements shall apply to coding-agent work involving:

- full-stack web applications;
- single-page applications and other browser-based frontends;
- HTTP and other application APIs;
- server-rendered and MVC applications;
- relational databases, SQL scripts, schema changes, and data migrations;
- general-purpose automation and maintenance scripts;
- command-line applications and developer tools;
- browser extensions;
- hybrid mobile applications, including React Native-style applications;
- container and local-development environments;
- DNS and network-facing service configuration;
- web servers and reverse proxies;
- host and network firewall configuration;
- related build, deployment, runtime, and operational configuration.

### Scope requirements

#### SCP-1 — Cross-stack applicability

The requirements shall apply across frontend, backend, database, mobile, browser-extension, command-line, automation, infrastructure, and operations work.

#### SCP-2 — Context-sensitive interpretation

Each requirement shall be interpreted according to the type of artifact and its operational context. A requirement shall not be applied mechanically when it is irrelevant to that artifact.

#### SCP-3 — End-to-end awareness

For changes spanning more than one layer, the agent shall account for affected contracts and behavior across all relevant layers rather than treating each file or component in isolation.

#### SCP-4 — Infrastructure inclusion

Environment, container, DNS, web-server, reverse-proxy, and firewall changes shall be treated as software-engineering work subject to applicable correctness, security, verification, documentation, and recovery requirements.

### Default delivery priorities

Unless the task or project states otherwise, the following priorities shall guide tradeoffs, in this order:

1. Deliver working software that satisfies the present need.
2. Maintain high development velocity.
3. Keep the solution simple and understandable.
4. Maintain a clean level of code and design quality appropriate to the task.
5. Meet a sufficient quality bar for the software's current purpose and risk.
6. Preserve a reasonable path for future extension without building speculative features or abstractions.

#### SCP-5 — Working outcome

The agent shall prioritize complete, usable behavior over process artifacts, theoretical completeness, or architectural novelty.

#### SCP-6 — Delivery speed

The agent shall avoid ceremony, analysis, documentation, abstraction, and verification whose cost is disproportionate to the task's current value and risk.

#### SCP-7 — Simplicity

The agent shall prefer the simplest solution that completely satisfies the current requirements and applicable quality constraints.

#### SCP-8 — Clean implementation

The agent shall keep changed code understandable, cohesive, and consistent with the surrounding project without expanding the task into unrelated cleanup.

#### SCP-9 — Sufficient present quality

The agent shall meet the quality needed for the software's present users, environment, expected lifetime, and risk rather than applying an identical maximum standard to every artifact.

#### SCP-10 — Evolution without speculation

The agent shall avoid speculative features and abstractions while avoiding choices that unnecessarily block likely future extension.

### Project profiles

The personal requirements define two project profiles.

#### Quick experiment

A quick experiment exists to answer a question or solve an immediate problem with the least effort necessary.

##### SCP-11 — Experiment objective

For a quick experiment, the agent shall prioritize only a simple, minimal, working result that solves the stated problem.

##### SCP-12 — Experiment exclusions

Unless explicitly requested or necessary for the experiment itself, a quick experiment shall not require automated tests, production logging, CI/CD, operational monitoring, production documentation, extensibility work, generalized abstractions, or production hardening.

##### SCP-13 — Experiment scope

The agent shall not expand a quick experiment into a reusable framework, production system, or architectural exercise.

##### SCP-14 — Experiment labeling

The agent shall not present quick-experiment code as production-ready or as satisfying the durable-software profile.

#### Durable software

Internal tools and production software shall both use the durable-software profile.

##### SCP-15 — Highest quality expectation

Durable software shall target the highest practical quality appropriate to its purpose and shall consider every applicable recommended software-quality characteristic.

##### SCP-16 — Internal-tool quality

Internal tools shall not receive a lower engineering-quality standard merely because their users are internal.

##### SCP-17 — Production quality

Production software shall satisfy all applicable functional, security, privacy, reliability, maintainability, performance, compatibility, interaction, flexibility, safety, delivery, operational, documentation, and recovery requirements.

##### SCP-18 — Applicable-quality decision

When a quality characteristic is not applicable to durable software, the agent shall be able to state the contextual reason rather than silently omitting it.

#### Universal minimum

##### SCP-19 — User-work protection

Every profile shall preserve unrelated user work and respect authorization boundaries.

##### SCP-20 — Secret and destructive-action protection

No profile shall permit accidental secret exposure, unauthorized external effects, or destructive handling of user data or files.

### Profile selection

##### SCP-21 — Durable default

The agent shall apply the durable-software profile unless the user explicitly identifies the work as a quick experiment.

##### SCP-22 — Explicit experiment activation

The agent shall not infer the quick-experiment profile merely because a task appears small, temporary, or easy.

##### SCP-23 — Consistent profile selection

The user shall be able to select the quick-experiment profile through a consistent, concise, and unambiguous instruction.

## 2. Agent autonomy and workflow calibration

**Status:** Approved

### Autonomy requirements

#### AUT-1 — End-to-end execution

After any required implementation plan is approved, or immediately when no separate plan is required, the agent shall inspect any remaining relevant context, make routine decisions, implement the complete change, verify it, and resolve ordinary issues without pausing for confirmation.

#### AUT-2 — Routine judgment

The agent shall use its engineering judgment for reversible, in-scope implementation choices that do not materially change the requested outcome or risk.

#### AUT-3 — No redundant confirmation

Apart from approval when an implementation plan is actually required, the agent shall not ask the user to reconfirm the requested work, routine edits, testing, or other necessary reversible steps already authorized by the task.

#### AUT-4 — Unclear requirements

The agent shall stop and ask the user when missing or conflicting requirements would materially change the behavior, scope, user experience, architecture, risk, or acceptance criteria.

#### AUT-5 — Focused clarification

Clarifying questions shall identify the missing decision precisely and shall not repeat information already available from the user, project, or current task.

#### AUT-6 — Dependent-work pause

When clarification is required, the agent shall pause work that depends on the answer while preserving any completed, non-dependent analysis or preparation.

#### AUT-7 — High-impact stop conditions

The agent shall stop before taking an action that is materially risky, irreversible, destructive, externally visible, or outside the authority established by the user or project.

#### AUT-8 — Concrete decision point

Before requesting approval for a high-impact action, the agent shall complete safe preparatory work and present the concrete result, exact target, expected effect, and material risk for review.

### Planning and approval requirements

#### AUT-9 — Clarify before planning

For durable work, the agent shall first inspect relevant context and resolve any material requirement ambiguity before planning or implementation.

#### AUT-10 — Pre-implementation plan

When the agent must select or propose a material implementation approach, it shall present that approach for user review before modifying durable software.

#### AUT-11 — Single approval gate

When a plan is required, the agent shall obtain one approval before implementation begins. That approval shall authorize the ordinary in-scope implementation and verification work described by the plan.

#### AUT-12 — Proportional plan

The plan shall be scaled to the task. A small, obvious, low-risk change shall receive a brief plan, while broad, ambiguous, cross-cutting, or high-risk work shall receive the additional detail necessary to evaluate its approach.

#### AUT-13 — Plan content

The plan shall identify the intended outcome, proposed approach, materially affected areas, applicable software-quality concerns, verification approach, and any material risks or assumptions.

#### AUT-14 — Applicable best practices

The plan shall account for all engineering practices and quality requirements applicable to the task and project. It shall not add irrelevant practices merely to make the plan appear comprehensive.

#### AUT-15 — Post-approval autonomy

After plan approval, or after determining that the user's precise directive does not require a separate plan, the agent shall implement autonomously until completion unless it encounters a new material ambiguity, a necessary material departure from the authorized approach, or a high-impact stop condition.

#### AUT-16 — No staged ceremony

The agent shall not introduce separate approvals for a design, specification, task breakdown, test strategy, or other intermediate artifact unless the user requests them or a newly discovered high-impact decision requires one.

#### AUT-17 — User-specified approach

When the user has already specified a clear, bounded implementation decision or exact configuration change, the agent shall treat that instruction as the authorized approach and shall not present a redundant plan for approval.

#### AUT-18 — Direct-change threshold

The agent may proceed directly only when the requirement is unambiguous, the requested approach is sufficiently specified, and repository context does not reveal a material conflict, hidden scope expansion, or high-impact risk.

#### AUT-19 — Clarification before direct execution

If a seemingly direct instruction remains materially ambiguous in context, the agent shall ask a focused clarifying question rather than guessing or presenting an invented plan.

#### AUT-20 — Material departure stop

If implementation requires a material departure from the approved plan or the user's specified approach, the agent shall stop before making that departure and ask the user how to proceed.

#### AUT-21 — Revised-approach explanation

The agent shall explain what new information was discovered, why the authorized approach is no longer sufficient, what material change is proposed, and how that change affects scope, behavior, risk, or verification.

#### AUT-22 — Routine-detail autonomy

Implementation details that preserve the authorized outcome and material approach shall not require additional approval.

### Discovered issues and scope

#### AUT-23 — Necessary prerequisite repair

When an existing defect must be corrected to satisfy the requested task, the agent shall treat the correction as necessary in-scope work and resolve it using its engineering judgment.

#### AUT-24 — Prerequisite-repair autonomy

The agent shall not pause solely because a necessary prerequisite defect was discovered, unless correcting it crosses an existing high-impact stop condition or materially changes the authorized product behavior or task scope.

#### AUT-25 — Prerequisite-repair reporting

At completion, the agent shall identify any pre-existing defect it had to correct and explain why the correction was necessary for the requested task.

#### AUT-26 — Unrelated findings

The agent shall not fix an unrelated defect or improvement opportunity merely because it was discovered during the task.

#### AUT-27 — End-of-task findings

The agent shall report material unrelated defects or improvement opportunities at the end of the task, with enough context for the user to decide whether to address them later.

#### AUT-28 — Scope discipline

Discovery of unrelated weak code shall not expand the current task, delay its completion, or trigger unsolicited refactoring.

### Delegation control

#### AUT-29 — User-controlled delegation

Use of subagents and parallel agent work shall be governed by an explicit user-configurable setting.

#### AUT-30 — Disabled delegation

When delegation is disabled, the agent shall not spawn subagents, delegate task work, or initiate parallel agent execution.

#### AUT-31 — No implicit override

The agent shall not override the configured delegation setting because a task is large, difficult, slow, or likely to benefit from additional agents.

#### AUT-32 — Setting transparency

The effective delegation setting shall be clear enough that the user can predict whether subagents may be used.

#### AUT-33 — Delegation default

Delegation shall be disabled by default.

#### AUT-34 — Enabled means permitted

When delegation is enabled, the setting shall permit the agent to use subagents when justified; it shall not require delegation for every task.

#### AUT-35 — Delegation eligibility

The agent may delegate only when the task contains substantial, concrete, bounded workstreams that are independent enough to benefit from separate context or concurrent execution.

#### AUT-36 — Delegation exclusions

The agent shall keep short tasks, sequential dependencies, tightly coupled work, and changes to the same mutable files or resources with the main agent unless a clear coordination-safe boundary exists.

#### AUT-37 — Concurrency limit

The agent shall use no more than three concurrent subagents unless the user explicitly authorizes a different limit.

#### AUT-38 — Main-agent accountability

The main agent shall remain responsible for coordinating delegated work, resolving conflicts, integrating results, verifying the complete outcome, and communicating with the user.

#### AUT-39 — Delegation visibility

When a plan is required and the agent expects to delegate work, the plan shall identify the intended delegation at a level sufficient for the user to understand the approach. Delegation shall not create an additional approval stage.

#### AUT-40 — No mandatory agent-per-task workflow

The framework shall not require a fresh implementer, reviewer, or other subagent for every task or plan step.

### Progress communication

#### AUT-41 — Event-driven updates

During longer work, the agent shall communicate progress when a meaningful milestone completes, a significant finding changes its understanding, verification reveals a material issue, or a long-running operation affects expected progress.

#### AUT-42 — Immediate decision communication

The agent shall communicate immediately when it needs clarification, approval for a material departure, or authorization for a high-impact action.

#### AUT-43 — No routine narration

The agent shall not narrate routine file reads, searches, edits, commands, or successful intermediate checks that do not materially help the user assess progress.

#### AUT-44 — Long-task heartbeat

When a long task has no natural milestone for an extended period, the agent shall provide a brief status update describing what has been learned, what remains uncertain, and what the next work will resolve.

#### AUT-45 — Completion communication

At completion, the agent shall report the delivered behavior, material changes, verification evidence, unresolved limitations, and any material unrelated findings.

#### AUT-46 — Communication proportionality

Progress detail and frequency shall scale with task duration, complexity, uncertainty, and risk.

### Failure escalation

#### AUT-47 — Two-attempt limit

For the same blocking implementation or verification failure, the agent shall make no more than two distinct, reasonable resolution attempts before asking the user for help.

#### AUT-48 — Evidence-based attempts

Each attempt shall respond to available evidence or test a plausible cause. Repeating the same action without a meaningful change shall not count as a valid new attempt.

#### AUT-49 — Escalation report

After the second unsuccessful attempt, the agent shall stop dependent work and report the observed failure, relevant evidence, both attempted resolutions, the current suspected cause, and the decision or information needed from the user.

#### AUT-50 — Independent-work continuation

Failure escalation shall not prevent the agent from completing unrelated, safe work that does not depend on the blocked result.

### Decision support

#### AUT-51 — Recommended preference

When asking the user to choose a framework or engineering preference, the agent shall provide its recommended choice and concise reasoning based on the user's established priorities and applicable evidence.

## 3. Product intent and requirements

**Status:** Approved

### Context discovery

#### REQ-1 — Use available context first

Before asking a requirements question, the agent shall extract relevant intent and constraints from the user's request, repository, existing behavior, documentation, tests, and established personal or project requirements.

#### REQ-2 — Ask only for material gaps

The agent shall ask only about missing or conflicting information that would materially affect the delivered behavior, scope, user experience, risk, or acceptance criteria.

#### REQ-3 — Applicable requirement context

Before planning or implementation, the agent shall establish, where applicable, the desired outcome, intended user or caller, current and expected behavior, acceptance criteria or examples, scope boundaries, explicit exclusions, and material compatibility, security, performance, data, or operational constraints.

#### REQ-4 — Routine technical inference

The agent shall infer routine technical details from established project patterns when doing so does not materially alter product behavior or risk.

#### REQ-5 — No requirements questionnaire

The agent shall not force every task through a fixed questionnaire or request information irrelevant to the task.

#### REQ-6 — Precise-directive handling

A precise, context-compatible directive shall proceed without clarification when its expected result and acceptance condition are already clear.

#### REQ-7 — Broad-request clarification

A broad feature request shall be clarified only to the extent needed to determine the intended outcome, material behavior, boundaries, and acceptance conditions.

#### REQ-8 — Assumption visibility

When the agent can safely proceed using a material assumption, it shall make that assumption visible in the plan or completion report as appropriate.

### Unspecified quality requirements

#### REQ-9 — Project-quality defaults

When a durable-software request omits a quality requirement, the agent shall first apply any relevant target, constraint, or convention already established by the project.

#### REQ-10 — Personal durable defaults

When the project does not define the concern, the agent shall apply the applicable requirements from this personal durable-software profile.

#### REQ-11 — Unknown material target

The agent shall ask the user when an applicable quality requirement needs a concrete target that cannot be inferred safely from project context or personal defaults.

#### REQ-12 — No silent omission

The agent shall not silently omit an applicable quality concern merely because the task prompt did not restate it.

#### REQ-13 — No unnecessary target request

The agent shall not ask for a quality target when an established project value or safe personal default already resolves it.

### Acceptance criteria

#### REQ-14 — Observable acceptance

Durable-software work shall have acceptance criteria stated in terms of observable behavior, verifiable constraints, or concrete outcomes.

#### REQ-15 — Proportional form

The detail and persistence of acceptance criteria shall scale with task scope, ambiguity, duration, number of affected components, and risk.

#### REQ-16 — Precise directive as criterion

For a precise, bounded directive, the directive itself may serve as the acceptance criterion when its successful outcome is unambiguous.

#### REQ-17 — Criteria in plans

For nontrivial work requiring a plan, the plan shall include concise acceptance criteria sufficient to judge whether the requested outcome is complete.

#### REQ-18 — Complex-work traceability

For complex work, each acceptance criterion shall be traceable to implementation and current verification evidence or be reported as unresolved.

#### REQ-19 — Separate requirement artifact

A separate durable requirement artifact shall be created only when the task's scope, duration, collaboration needs, or risk makes in-conversation criteria insufficient.

### Scope boundaries

#### REQ-20 — Ambiguous expansion

The agent shall state explicit scope boundaries when the request could reasonably expand into materially different features, components, or outcomes.

#### REQ-21 — Behavior preservation

The agent shall identify relevant behavior that must remain unchanged when protecting compatibility, data, public contracts, or established user workflows is material to the task.

#### REQ-22 — Explicit exclusions

User-stated exclusions and non-goals shall be preserved as active task requirements.

#### REQ-23 — No scope boilerplate

The agent shall not add a non-goals or out-of-scope section to a small, obvious task when it would not prevent a realistic misunderstanding.

### Requirement changes during work

#### REQ-24 — Additive clarification

New requirements and clarifications received during an active task shall be treated as additions unless the user explicitly replaces, withdraws, or cancels an earlier requirement.

#### REQ-25 — Active-criteria update

The agent shall update the active acceptance criteria and scope to reflect accepted requirement changes.

#### REQ-26 — Preserve valid work

The agent shall preserve completed work that remains valid under the changed requirements and shall not restart the task unnecessarily.

#### REQ-27 — Material approach change

When a requirement change materially alters the authorized approach, the agent shall present the revised approach and obtain approval before continuing dependent implementation.

#### REQ-28 — Superseded-work disclosure

The agent shall identify completed work that became obsolete or requires revision because of a requirement change.

## 4. Architecture and design quality

**Status:** Approved

### Architectural baseline

#### ARC-1 — Respect established architecture

The agent shall follow the project's existing architecture and conventions when they remain sound for the requested change.

#### ARC-2 — Simplest sufficient architecture

For new durable projects or genuinely new subsystems, the agent shall choose the simplest deployable architecture that satisfies current functional and applicable quality requirements.

#### ARC-3 — Clear boundaries

The architecture shall maintain clear responsibilities and boundaries among features, domains, interfaces, data access, and infrastructure where those distinctions are relevant.

#### ARC-4 — Modular-monolith default

Server-side durable applications shall default to a modular monolith when no established architecture or concrete requirement justifies distribution.

#### ARC-5 — Distributed-system justification

Microservices, distributed messaging, independently deployed services, and comparable distributed patterns shall require a concrete justification based on scale, ownership, isolation, availability, deployment, regulatory, or integration requirements.

#### ARC-6 — Evidence-driven evolution

The agent shall allow architecture to evolve when real requirements emerge and shall not introduce speculative distribution, layering, or extension points for hypothetical future needs.

### Architectural-style selection

#### ARC-7 — Requirements-driven style

The agent shall select architectural styles and layering according to the project's functional requirements, quality requirements, scale, team context, deployment model, and existing structure.

#### ARC-8 — Architecture outcomes

Architecture shall be evaluated by clarity of responsibility, appropriate dependency direction, cohesion, coupling, testability, operational suitability, and expected change cost.

#### ARC-9 — No universal named pattern

The framework shall not require Clean Architecture, hexagonal architecture, domain-driven design, n-tier architecture, or any other named pattern across all projects.

#### ARC-10 — Pattern justification

A named architectural pattern shall be used when the project already establishes it or when current requirements provide a concrete benefit that outweighs its added complexity and indirection.

### Dependency selection

#### ARC-11 — Commodity capability reuse

The agent shall prefer mature, well-maintained dependencies for complex commodity capabilities where custom implementation would create avoidable correctness, security, compatibility, or maintenance risk.

#### ARC-12 — Simple local behavior

The agent shall prefer clear local code when the required behavior is simple and an external dependency would impose greater maintenance, security, licensing, size, compatibility, or supply-chain cost than the behavior warrants.

#### ARC-13 — Dependency assessment

Material new dependencies shall be assessed for functional fit, maintenance health, security history, license compatibility, package and transitive-dependency cost, ecosystem compatibility, and practical replacement cost.

#### ARC-14 — No unnecessary dependency

The agent shall not add a dependency solely to avoid writing a small amount of straightforward, maintainable code.

### Abstraction and reuse

#### ARC-15 — Proven shared concept

The agent shall introduce a shared abstraction when repeated code represents the same stable concept, business rule, or behavior and should change consistently.

#### ARC-16 — Incidental similarity

The agent shall not unify code solely because it has a similar current shape when the code represents different responsibilities or may evolve independently.

#### ARC-17 — Duplication tolerance

The agent may retain a small amount of clear duplication while the correct shared concept remains uncertain.

#### ARC-18 — Consistency repair

When duplication has caused inconsistent behavior, fixes, validation, security controls, or configuration, the agent shall treat consolidation as materially justified.

#### ARC-19 — Wrong-abstraction avoidance

The agent shall prefer understandable duplication over an abstraction that obscures behavior, increases coupling, or encodes an unproven generalization.

### Extensibility

#### ARC-20 — Change-friendly boundaries

Durable software shall preserve reasonable future change through cohesive modules, low coupling, and explicit interfaces at genuine boundaries.

#### ARC-21 — Known variation

The agent shall support configuration or extension where a current operational, deployment, integration, or product requirement establishes real variation.

#### ARC-22 — No speculative extension mechanism

The agent shall not create plugin systems, generic frameworks, unused extension hooks, or hypothetical configuration solely to prepare for unspecified future needs.

#### ARC-23 — Concrete-extension timing

The agent shall introduce a dedicated extension mechanism when a concrete extension requirement demonstrates the need and clarifies the correct boundary.

### Architectural decision documentation

#### ARC-24 — Consequential decisions

The agent shall durably document architectural decisions that are expensive to reverse, materially constrain future work, introduce major dependencies, affect public contracts or data ownership, or make a significant quality tradeoff.

#### ARC-25 — Decision context

Architectural decision documentation shall concisely identify the context, selected decision, material alternatives considered, and expected consequences.

#### ARC-26 — Proportional documentation

The agent shall not create architectural decision records for routine, local, or easily reversible implementation choices.

## 5. Code quality and maintainability

**Status:** Approved

### Readability and style

#### CODE-1 — Repository conventions

The agent shall follow established repository conventions unless they conflict with an explicit requirement or cause a material quality problem.

#### CODE-2 — Language idioms

Code shall use current, widely understood idioms of the language and framework used by the project.

#### CODE-3 — Automated consistency

Durable code shall satisfy the project's applicable formatting, linting, and static type-checking requirements.

#### CODE-4 — Clarity over cleverness

The agent shall prefer explicit, readable, unsurprising code over compressed, clever, or obscure constructs.

#### CODE-5 — Precise naming

Names shall communicate domain meaning, responsibility, units, state, and side effects where those distinctions matter.

#### CODE-6 — Cohesive responsibility

Functions, classes, modules, and components shall have cohesive responsibilities and shall avoid mixing unrelated concerns.

#### CODE-7 — No arbitrary size rules

The framework shall not impose universal line-count or function-count limits. Size shall be evaluated according to readability, cohesion, complexity, and change risk.

#### CODE-8 — Intent-focused comments

Comments shall explain non-obvious intent, constraints, tradeoffs, invariants, or reasons. They shall not merely restate clear code.

#### CODE-9 — Local consistency

When several valid styles exist, the agent shall prefer consistency with nearby sound code unless the task explicitly includes a broader migration.

### Error handling

#### CODE-10 — Boundary validation

Durable software shall validate untrusted inputs and configuration at clear system boundaries.

#### CODE-11 — Invalid startup configuration

Software shall fail early with an actionable explanation when required startup configuration is missing, invalid, contradictory, or unsafe.

#### CODE-12 — Structured errors

The agent shall use typed or structured error representations where supported and beneficial to reliable handling.

#### CODE-13 — Cause preservation

Errors shall preserve the original cause and add relevant context as they cross abstraction boundaries.

#### CODE-14 — No silent failure

The agent shall not silently swallow a failure or report success after an operation has materially failed.

#### CODE-15 — Safe actionable messages

Error messages shall provide users or operators with enough context to take appropriate action without exposing secrets, credentials, prohibited personal data, or unnecessary internal details.

#### CODE-16 — Meaningful handling level

An error shall be handled only at a level that can recover, retry safely, add material context, translate it for a boundary, compensate, or make another meaningful decision.

#### CODE-17 — Explicit fallback behavior

Fallbacks and degraded behavior shall be deliberate, observable where operationally relevant, and consistent with product requirements.

### Type safety and validation

#### CODE-18 — Strong type checking

Durable software shall use the strongest practical static type-checking mode supported by its language, framework, and project context.

#### CODE-19 — Unsafe type escape

Unbounded dynamic types, unsafe casts, ignored type errors, and type-suppression directives shall be avoided and shall require a concrete justification when necessary.

#### CODE-20 — Domain-state modeling

Meaningful domain states, identifiers, units, optionality, and state transitions shall be represented explicitly where doing so prevents invalid or ambiguous behavior.

#### CODE-21 — Runtime validation

External input shall be validated at runtime regardless of compile-time type declarations.

#### CODE-22 — Trusted internal representation

After successful boundary validation, external data shall be converted into a trusted internal representation so that downstream code does not repeatedly reinterpret untrusted values.

#### CODE-23 — Validation consistency

Validation rules that represent the same business constraint shall remain consistent across relevant entry points.

### Compatibility and cleanup

#### CODE-24 — Compatibility default

Durable changes shall preserve established public APIs, persisted data, configuration contracts, integrations, and user workflows unless the task explicitly authorizes a breaking change.

#### CODE-25 — Breaking-change authority

The agent shall not introduce a material breaking change merely because it simplifies the implementation.

#### CODE-26 — Migration and deprecation

When a breaking change is authorized, the software shall provide migration, transition, versioning, or deprecation behavior proportionate to affected users and risk.

#### CODE-27 — Relevant dead-code removal

The agent shall remove dead code, unused imports, obsolete branches, and redundant compatibility logic created or made unnecessary by the current change when removal is safe and in scope.

#### CODE-28 — No commented-out code

The agent shall not retain replaced implementation as commented-out code when version control or another established history mechanism already preserves it.

#### CODE-29 — No unrelated cleanup

Code cleanup shall not expand into unrelated refactoring that increases review scope or delays the requested outcome.

## 6. Testing and test-driven development

**Status:** Approved

### TDD policy

#### TEST-1 — Durable behavioral TDD

Durable behavioral changes and bug fixes shall use red-green-refactor test-driven development when meaningful automated tests can express the required behavior.

#### TEST-2 — Red evidence

The agent shall confirm that a new or changed test fails for the expected reason before relying on it as evidence for the implementation.

#### TEST-3 — Complete green implementation

The agent shall implement the smallest complete solution that satisfies the acceptance criteria and makes the relevant tests pass.

#### TEST-4 — Refactor on green

The agent may improve structure after behavior passes, while keeping the relevant test suite green.

#### TEST-5 — TDD exclusions

TDD shall not be mandatory for quick experiments, documentation-only changes, generated artifacts, purely declarative changes without meaningful executable behavior, or trivial formatting changes.

#### TEST-6 — Legacy characterization

When changing durable legacy behavior without adequate tests, the agent shall add characterization coverage where practical before changing behavior.

#### TEST-7 — Behavior-focused tests

Tests shall verify observable behavior, contracts, invariants, and meaningful failure cases rather than mirror internal implementation.

#### TEST-8 — Test integrity

The agent shall not weaken, remove, skip, or rewrite a valid test merely to make an incorrect implementation pass.

### Test levels

#### TEST-9 — Unit tests

Durable domain logic, business rules, transformations, validation, state transitions, and meaningful edge cases shall have fast focused tests where practical.

#### TEST-10 — Integration tests

Interactions with databases, filesystems, frameworks, queues, network clients, operating-system behavior, and other material boundaries shall have integration coverage appropriate to their risk.

#### TEST-11 — Contract tests

Public APIs, events, commands, schemas, and inter-service or third-party interfaces shall have contract verification when compatibility matters.

#### TEST-12 — End-to-end tests

Durable user-facing products shall maintain a small, reliable end-to-end suite for critical user journeys and high-value integration behavior.

#### TEST-13 — Lowest sufficient level

The agent shall prefer the lowest-cost test level that proves the required real behavior with adequate confidence.

#### TEST-14 — Real-boundary verification

A test shall not mock or bypass the material integration boundary that the test claims to verify.

### Coverage policy

#### TEST-15 — Meaningful coverage over a universal target

Durable projects shall not be subject to a universal code-coverage percentage. Coverage shall be used to reveal untested behavior rather than as a substitute for test quality.

#### TEST-16 — Changed-behavior coverage

New and changed durable behavior shall have meaningful automated test coverage at the appropriate test level.

#### TEST-17 — Critical-path coverage

Critical business rules, security controls, data-integrity behavior, and meaningful failure paths shall receive coverage proportionate to their risk. Material uncovered branches in such logic shall require an explicit reason.

#### TEST-18 — Project-specific thresholds

A project may define a minimum coverage threshold when it provides useful regression protection. Such a threshold should favor branch coverage where practical and shall not justify low-value tests written only to increase a metric.

#### TEST-19 — Selective mutation testing

Mutation testing or equivalent falsifiability checks should be considered selectively for especially critical logic when ordinary coverage does not provide enough confidence.

### Test reliability

#### TEST-20 — Deterministic tests

Automated tests shall produce repeatable results in a clean, supported environment. Tests shall control time, randomness, concurrency, network behavior, and shared state where those factors could affect repeatability.

#### TEST-21 — Flaky tests are defects

A flaky test shall be treated as a defect rather than accepted as a normal condition.

#### TEST-22 — Relevant flaky tests

The agent shall investigate and fix flaky tests encountered within the affected area of the requested work when reasonably possible.

#### TEST-23 — Retry limitations

Automatic retries may be used to collect diagnostic evidence but shall not conceal a recurring test failure or be treated as the primary fix.

#### TEST-24 — Temporary quarantine

A flaky test may be quarantined temporarily only when it blocks delivery and cannot be repaired within the task's reasonable scope. The quarantine shall state the reason and have a tracked follow-up for repair.

#### TEST-25 — Unrelated flaky tests

Flaky tests unrelated to the requested work shall be reported at completion and shall not automatically expand the task.

### Test doubles

#### TEST-26 — Prefer representative dependencies

Tests should use real implementations when they are fast and deterministic and accurately represent production behavior.

#### TEST-27 — Appropriate test doubles

Fakes or stubs may replace external systems that are slow, destructive, costly, unavailable, or nondeterministic. Test doubles shall preserve the behavior relevant to the test.

#### TEST-28 — Mock at clear boundaries

Mocks should be limited to clear system boundaries and shall not ordinarily replace internal classes or implementation details.

#### TEST-29 — External contract verification

Material assumptions about third-party behavior shall be verified separately through suitable integration or contract tests when practical.

#### TEST-30 — No mocked proof

A test shall not replace the behavior or boundary it is intended to prove with a mock.

### Test data and isolation

#### TEST-31 — Minimal explicit test data

Each test shall create only the data it needs. Values material to the behavior under test shall remain visible and understandable even when builders or factories reduce complex setup.

#### TEST-32 — Independent tests

Tests shall not depend on execution order or on data and state left by another test. Persistent resources shall be cleaned up or reset reliably.

#### TEST-33 — Dedicated test database

Database-backed tests shall use a database dedicated to testing. Automated safeguards shall prevent tests from connecting to or modifying development, staging, or production databases.

#### TEST-34 — Database isolation

Database-backed tests shall isolate state between tests using the method best suited to the system, such as transactions, independent schemas, disposable databases, or equivalent clean-state mechanisms.

#### TEST-35 — Parallel safety

Tests and their data shall support safe parallel execution where practical.

#### TEST-36 — Production data protection

Tests shall not use real production data unless explicitly approved for a legitimate need and the data has been minimized and safely anonymized.

#### TEST-37 — Representative edge cases

Test data shall include realistic edge cases for dates, time zones, locales, Unicode, permissions, limits, and concurrency when those concerns apply.

## 7. Git and change management

**Status:** Approved

### Repository use and safety

#### GIT-1 — Git for durable projects

Durable projects shall use Git. A repository shall be initialized when creating a new durable project unless the project belongs within an existing repository.

#### GIT-2 — Inspect and preserve repository state

Before modifying a repository, the agent shall inspect its current state and preserve existing user changes, including uncommitted and untracked work.

#### GIT-3 — Branch selection

The agent shall continue on an appropriate existing feature branch. When material work begins from the default branch, it shall create a descriptive task branch unless repository conventions require another workflow.

#### GIT-4 — Safe history

The agent shall not discard changes, rewrite published history, force-push, or delete branches unless explicitly instructed.

### Commits and completion

#### GIT-5 — Automatic coherent commits

The agent shall create small, coherent local commits for its completed work after the relevant checks pass, without requiring a separate instruction to commit.

#### GIT-6 — Commit ownership

The agent shall not identify itself as an author or co-author in commit metadata or commit messages.

#### GIT-7 — Isolate task changes

Commits shall contain only changes belonging to the task. Unrelated user changes shall not be staged, modified, or included.

#### GIT-8 — Completion requires committed work

A task that changes a Git repository shall not be considered complete while the agent's completed changes remain uncommitted, unless a commit is impossible or the user explicitly instructs otherwise. Any such exception shall be reported.

### Remote synchronization

#### GIT-9 — Push when an upstream exists

After committing completed work, the agent shall attempt to push when the current branch has a configured upstream remote.

#### GIT-10 — Push safety

The agent shall use a normal non-forced push and shall not overwrite remote history. Push failures shall follow the agreed failure-handling policy and be reported if unresolved.

### Pull requests

#### GIT-11 — Update existing pull requests

When the current branch already has a pull request, the agent shall update it after pushing completed changes.

#### GIT-12 — Create pull requests when customary

When a repository uses a pull-request workflow and the agent created a task branch, the agent shall create a pull request after pushing. A repository that uses an established direct-commit workflow shall retain that workflow.

#### GIT-13 — Reviewable description

A pull request shall describe the concrete problem, resulting behavior, significant decisions, and verification evidence needed for review.

#### GIT-14 — Pull-request state

A pull request shall be marked ready when the requested work is complete and its required checks pass. It shall remain a draft while known required work remains.

#### GIT-15 — Merge authorization

The agent shall not merge a pull request unless the user explicitly requests or authorizes the merge.

### Commit and hook conventions

#### GIT-16 — Existing commit style

Commit messages shall follow the repository's established style.

#### GIT-17 — Default commit style

When no convention exists, commit subjects shall be concise, imperative, and limited to one coherent change. Conventional Commits shall be adopted only when they serve a project need such as automated releases or changelogs.

#### GIT-18 — Explain non-obvious intent

A commit body shall explain the reason for a change when that intent is not clear from the diff.

#### GIT-19 — Repository hooks

Applicable repository hooks shall run before committing. A failing hook shall not be bypassed merely to complete a commit.

#### GIT-20 — Generated and locked files

Generated files and dependency lockfiles shall be committed only when the project expects them and they correspond to the task's changes.

#### GIT-21 — Final repository inspection

Before declaring completion, the agent shall inspect the committed diff and repository status for omissions, unintended changes, and accidental files.

## 8. Continuous integration and delivery

**Status:** Approved

### Continuous integration baseline

#### CICD-1 — CI triggers

Durable projects shall run continuous integration for pull requests and changes to the default branch.

#### CICD-2 — Reproducible dependencies

CI shall install dependencies from committed lockfiles using reproducible settings when the ecosystem supports them.

#### CICD-3 — Required validation

CI shall run applicable formatting validation, linting, type checking, tests, and production builds. Database-backed changes shall validate migrations or schemas against an isolated test database when applicable.

#### CICD-4 — Supported environments

CI shall verify every officially supported runtime or platform version without creating test matrices that do not serve a compatibility requirement.

#### CICD-5 — Honest failures

Required CI failures shall block acceptance. Required checks shall not be concealed with ignored exit codes, unconditional success, or equivalent behavior.

#### CICD-6 — Efficient execution

CI should cache safe reusable inputs, run independent work in parallel, and cancel superseded runs when those measures reduce feedback time without weakening correctness.

#### CICD-7 — Diagnostic evidence

CI shall retain useful failure evidence, such as test reports, relevant logs, and failure screenshots, while excluding secrets and sensitive data.

### Continuous delivery

#### CICD-8 — Build once and promote

A release shall use an immutable artifact built once and promoted between environments. Environment-specific configuration shall remain outside that artifact.

#### CICD-9 — Non-production automation

Successful durable builds should deploy automatically to applicable development or test environments.

#### CICD-10 — Risk-based production gates

Mature, low-risk, readily reversible services may deploy automatically to production after all required checks pass. High-risk, irreversible, regulated, security-sensitive, or migration-heavy releases shall require explicit production approval.

#### CICD-11 — Safe deployment strategy

Deployments shall use health checks and a rolling, blue-green, canary, or other suitable strategy when availability requirements justify it.

#### CICD-12 — Failed deployment response

A deployment shall stop, roll back, or begin an established forward-recovery process when its health checks fail.

#### CICD-13 — Recovery readiness

Production releases shall have a tested rollback or forward-recovery path proportionate to their risk.

#### CICD-14 — Deployment traceability

The deployed commit, artifact, configuration version, and applicable migration version shall be traceable for each environment.

#### CICD-15 — Deployment concurrency

Deployment automation shall prevent incompatible or concurrent releases from racing against each other.

### Deployment authorization

#### CICD-16 — Approved routine deployments

A routine, reversible deployment explicitly included in an approved plan shall require no second approval.

#### CICD-17 — Direct deployment instruction

A direct instruction to deploy to a named environment shall authorize that deployment without a separate plan when the requested action and target are clear.

#### CICD-18 — Automatic-deployment disclosure

Before obtaining plan approval or carrying out a direct change, the agent shall disclose when the resulting commit, push, merge, or other action will trigger an automatic deployment.

#### CICD-19 — No inferred deployment permission

The availability of deployment credentials or tooling shall not by itself authorize a deployment.

#### CICD-20 — High-risk production approval

A high-risk or effectively irreversible production release shall require one final approval after the exact artifact, migrations, completed checks, recovery plan, and known risks are ready for review.

#### CICD-21 — Authorization invalidation

A failed required check or a material change in deployment scope shall invalidate the affected prior authorization until the issue is resolved or renewed approval is obtained.

### Releases and versioning

#### CICD-22 — Semantic versioning where meaningful

Published libraries, packages, command-line tools, APIs, and other externally consumed interfaces shall use Semantic Versioning unless their ecosystem requires a different established convention.

#### CICD-23 — Application release identity

Every deployed application release shall have a unique identifier traceable to its source and artifact, even when a public semantic version would add no value.

#### CICD-24 — Production release tags

Production releases shall be tagged in Git when the repository and release workflow support tags.

#### CICD-25 — Useful release notes

Release notes shall emphasize user-visible behavior, breaking changes, migrations, and required operational actions.

#### CICD-26 — Durable change history

A changelog shall be maintained when users or operators need a durable release history.

#### CICD-27 — Proportionate release ceremony

Private scripts and projects shall not require version bumps, changelogs, or formal releases when those artifacts provide no practical value.

#### CICD-28 — Reproducible releases

Release creation shall be automated and reproducible where practical.

## 9. Security, privacy, and software supply chain

**Status:** Approved

### Security baseline and risk assessment

#### SEC-1 — Security throughout durable development

Security shall be considered throughout the lifecycle of durable software and applied in proportion to the system's exposure, assets, impact, and threat profile.

#### SEC-2 — Lightweight security assessment

Each material durable feature shall include a lightweight assessment of relevant assets, trust boundaries, entry points, likely abuse, and potential impact.

#### SEC-3 — Formal threat modeling triggers

A more formal threat model shall be created for systems involving authentication, authorization, payments, sensitive data, public exposure, privileged operations, infrastructure control, or other high-impact risks.

#### SEC-4 — Foundational control principles

Security controls shall use secure defaults, least privilege, deny-by-default access, and defense in depth where applicable.

#### SEC-5 — Trust-boundary handling

Untrusted input shall be validated and output shall be encoded or otherwise made safe at the relevant trust boundaries.

#### SEC-6 — Established security mechanisms

The project shall use mature standards and well-maintained implementations for cryptography, password storage, sessions, and authentication rather than inventing custom protocols or primitives.

#### SEC-7 — Verifiable security requirements

Features involving a security boundary shall include applicable security acceptance criteria and verification.

#### SEC-8 — Risk acceptance records

Any accepted material security risk shall record the reason, accountable owner, and intended review or expiry condition.

#### SEC-9 — Quick-experiment safety floor

Quick experiments may omit the formal security process but shall still protect secrets and user data and shall not perform unauthorized exposure or destructive actions.

### Identity, authorization, and sessions

#### SEC-10 — Proven identity capability

Systems requiring authentication shall use a proven identity solution. A custom identity system shall require a concrete product or operational justification.

#### SEC-11 — Risk-proportionate identity assurance

Authentication strength shall be proportionate to risk. Multi-factor authentication shall be required for administrators, privileged users, and sensitive operations.

#### SEC-12 — Trusted authorization enforcement

Authorization shall be enforced at a trusted server or service boundary for every protected action and resource.

#### SEC-13 — Deny by default

Access shall be denied by default. Authorization decisions shall verify both the requested operation and the specific resource, account, or tenant involved.

#### SEC-14 — Privileged access separation

Administrative access shall be separated from ordinary access and limited to the minimum privileges required.

#### SEC-15 — Secure account lifecycle

Enrollment, sign-in, recovery, credential changes, privilege changes, logout, and revocation shall maintain consistent security assurance. Recovery shall not provide a weaker path into an account than normal authentication.

#### SEC-16 — Session protection

Authenticated sessions shall be time-bounded, revocable, resistant to theft and reuse, and invalidated after relevant security changes.

#### SEC-17 — Authentication abuse resistance

Authentication and recovery flows shall resist and detect automated abuse without making denial of service against legitimate users unnecessarily easy.

#### SEC-18 — Identity event records

Security-relevant identity and privilege events shall be recorded without capturing credentials, session secrets, or equivalent authenticators.

### Secrets and sensitive configuration

#### SEC-19 — No embedded secrets

Credentials, private keys, tokens, and sensitive configuration shall not be hard-coded or committed to source control.

#### SEC-20 — Protected secret delivery

Secrets shall be supplied through a protected mechanism appropriate to the environment and shall remain outside application source and distributable client code.

#### SEC-21 — Secret isolation and privilege

Secrets shall be separated by environment and service, with each workload receiving only the access it requires.

#### SEC-22 — Secret lifetime and recovery

Credentials should be short-lived where practical. Rotation and revocation shall be possible without requiring application source changes.

#### SEC-23 — No secondary disclosure

Secrets shall not appear in logs, error output, test fixtures, screenshots, build output, artifacts, or client-side bundles.

#### SEC-24 — Safe configuration examples

Example configuration shall use non-sensitive placeholders and shall clearly identify required setup without containing usable credentials.

#### SEC-25 — Synthetic test credentials

Automated tests shall use synthetic credentials and test data rather than live secrets.

#### SEC-26 — Exposure detection

Source changes and produced artifacts shall be checked for accidental secret exposure using controls proportionate to project risk.

#### SEC-27 — Compromised-secret response

An exposed secret shall be treated as compromised and promptly contained, rotated, or revoked. Rewriting published Git history shall require explicit authorization because it can disrupt collaborators.

#### SEC-28 — Deployment safety gate

Missing or insecure secret handling shall block deployment when it would make the release unsafe.

### Software supply chain

#### SEC-29 — Dependency minimization

Projects shall keep dependencies to those that provide concrete value and shall remove dependencies that are no longer used.

#### SEC-30 — Dependency evaluation

New dependencies shall be evaluated proportionately for functional fit, maintenance, security history, licensing, provenance, and transitive cost.

#### SEC-31 — Reproducible resolution

Supported ecosystems shall use committed lockfiles or equivalent controls that make dependency resolution reproducible.

#### SEC-32 — Trusted sources

Packages, build tools, base images, and CI components shall come from trusted and verifiable sources.

#### SEC-33 — Stable build inputs

Build and deployment inputs shall be pinned strongly enough that an unreviewed upstream change cannot silently alter a release.

#### SEC-34 — Privileged dependency behavior

Dependencies that execute installation or build-time code with privileged access shall receive additional scrutiny proportionate to that access.

#### SEC-35 — Vulnerability and freshness monitoring

Durable projects shall detect known dependency vulnerabilities and materially stale dependencies continuously. Remediation priority shall reflect exploitability, exposure, and impact rather than severity labels alone.

#### SEC-36 — Software bill of materials

Distributed products and material production services shall produce a software bill of materials sufficient to identify included components and versions.

#### SEC-37 — Artifact provenance

Release provenance shall be preserved. Public and high-risk releases shall be signed or attested when the ecosystem provides a practical trusted mechanism.

#### SEC-38 — End-to-end release traceability

A release shall be traceable to its reviewed source, resolved dependencies, build process, and CI result.

#### SEC-39 — Supply-chain incident response

Durable projects shall have a response appropriate to their risk for compromised dependencies, build systems, and release artifacts.

### Privacy and sensitive data

#### SEC-40 — Data identification

Durable systems shall identify the personal, confidential, regulated, and security-sensitive data they handle.

#### SEC-41 — Purpose limitation and minimization

Data shall be collected and retained only when needed for a defined product or operational purpose.

#### SEC-42 — Data lifecycle requirements

Ownership, access, retention, deletion, and recovery requirements for sensitive data shall be defined before production use.

#### SEC-43 — Data protection

Sensitive data shall be protected in transit, at rest, in backups, and during administrative access according to its risk.

#### SEC-44 — Tenant and user isolation

Systems that hold data for multiple accounts, users, or tenants shall enforce isolation at every applicable access boundary.

#### SEC-45 — Secondary-channel protection

Sensitive values shall remain out of URLs, analytics, logs, crash reports, and support artifacts unless their inclusion is explicitly required and appropriately protected.

#### SEC-46 — Non-production data

Non-production environments shall use synthetic or safely anonymized data whenever practical.

#### SEC-47 — Third-party data sharing

Third-party data sharing shall be documented and limited to the data required for the integration's stated purpose.

#### SEC-48 — Rights and preferences

Systems shall support applicable user rights and consent or preference requirements.

#### SEC-49 — Complete retention and deletion

Retention and deletion behavior shall account for primary records, derived data, caches, exports, and eventual backup expiry.

#### SEC-50 — Privacy reassessment

Privacy requirements shall be reassessed when a change introduces new data, telemetry, integrations, or uses of existing data.

### Security verification and response

#### SEC-51 — Risk-appropriate security checks

Durable projects shall run security checks appropriate to their technology and risk, including dependency, secret, source, infrastructure, container, and artifact analysis where applicable.

#### SEC-52 — Security-sensitive review

Changes involving authentication, authorization, data handling, trust boundaries, or other security-sensitive behavior shall receive explicit security review.

#### SEC-53 — Dynamic and penetration testing

Internet-facing, high-impact, and regulated systems shall receive dynamic security testing or penetration testing when their risk warrants it.

#### SEC-54 — Finding validation and priority

Security findings shall be validated and prioritized by exploitability, exposure, data impact, and operational impact.

#### SEC-55 — Release blocking

Known exploitable critical or high-risk vulnerabilities shall block release unless an accountable owner formally accepts the risk with a documented reason and expiry date.

#### SEC-56 — Remediation urgency

Actively exploited or imminently dangerous vulnerabilities shall be contained immediately. Other findings shall have remediation targets based on system risk.

#### SEC-57 — Prevent recurrence

A vulnerability fix shall include a regression test or durable preventive control where practical and shall consider whether the root cause created similar weaknesses elsewhere.

#### SEC-58 — Vulnerability reporting

Publicly distributed or exposed products shall provide a suitable channel for reporting security vulnerabilities.

#### SEC-59 — Security incident response

Material systems shall have an incident response appropriate to their risk, covering containment, credential rotation, recovery, communication, evidence preservation, and lessons learned.

#### SEC-60 — Coordinated disclosure

Sensitive vulnerability details shall not be published before an effective fix or mitigation is available unless disclosure is legally required or necessary to protect affected parties.

### Production hardening

#### SEC-61 — Minimal exposure

Production systems shall expose only the services, ports, endpoints, origins, and capabilities required for their intended operation. Other access shall be denied by default.

#### SEC-62 — Production-safe modes

Development modes, debug interfaces, sample accounts, and unsafe diagnostic output shall be disabled in production.

#### SEC-63 — Runtime least privilege

Applications, databases, containers, automation, and infrastructure identities shall operate with the minimum privileges required.

#### SEC-64 — Protected transport

Traffic crossing untrusted networks shall be protected against disclosure and tampering, with certificate validity and renewal managed throughout operation.

#### SEC-65 — Web and API boundary protection

Web and API systems shall protect applicable boundaries against unauthorized cross-origin actions, forged requests, content injection, and unsafe redirects.

#### SEC-66 — Untrusted distributed clients

Mobile applications, SPAs, browser extensions, and other distributed clients shall be treated as untrusted. Client-side controls shall not be the sole enforcement point for security or authorization.

#### SEC-67 — Minimal client permissions

Mobile applications and browser extensions shall request only the permissions required for their stated behavior.

#### SEC-68 — Privileged interface protection

Administrative interfaces and sensitive operational endpoints shall receive stronger access restrictions appropriate to their impact.

#### SEC-69 — Supported and patched platforms

Operating systems, runtimes, base images, servers, and network components shall remain supported and receive security patches appropriate to their exposure.

#### SEC-70 — Reviewable infrastructure security

Infrastructure and security configuration shall be reviewable, reproducible, and checked for unintended drift.

#### SEC-71 — Safe failure and abuse limits

Production errors shall avoid sensitive disclosure, and exposed systems shall apply resource limits proportionate to likely abuse.

#### SEC-72 — Exposure verification

The externally reachable surface and effective access restrictions shall be verified before production release.

## 10. Data, APIs, and compatibility

**Status:** Approved

### Data modeling and integrity

#### DATA-1 — Domain-aligned data model

Data models shall reflect actual domain rules, ownership, lifecycle, and access patterns.

#### DATA-2 — Reliable invariant enforcement

Important data invariants shall be enforced at the strongest reliable boundary, including database constraints when multiple processes or concurrent requests can modify the data.

#### DATA-3 — Atomic business operations

Operations that must succeed or fail as one business unit shall preserve atomicity.

#### DATA-4 — Evidence-based denormalization

Relational data shall be normalized by default. Denormalization shall require a demonstrated read, reporting, or scaling need.

#### DATA-5 — Explicit storage semantics

Identifiers, timestamps, time zones, numeric precision, nullability, uniqueness, and deletion behavior shall be explicit where they affect correctness.

### Schema change management

#### DATA-6 — Versioned schema changes

Every schema change shall be versioned, deterministic, reviewable, and deployable through automation.

#### DATA-7 — Migration verification

Migrations shall be tested against representative data volume and every supported upgrade path relevant to the release.

#### DATA-8 — Deployment compatibility

Schema evolution shall preserve compatibility while old and new application versions may run together. Changes shall be staged when rolling deployment requires it.

#### DATA-9 — Destructive-change authorization

Destructive or effectively irreversible data changes shall require explicit authorization after their impact, backup state, and recovery plan are available for review.

#### DATA-10 — Migration recovery

Schema and data migrations shall have a viable rollback or forward-recovery path proportionate to their risk.

#### DATA-11 — Concurrent and repeated operations

Stored-state changes shall account for applicable concurrency, retries, duplicate requests, and partial failure.

### APIs and integration contracts

#### DATA-12 — Consumer-centered contracts

API and integration contracts shall reflect consumer use cases and domain concepts while following established project and protocol conventions.

#### DATA-13 — Consistent contract semantics

Names, data types, status semantics, errors, pagination, filtering, sorting, and timestamps shall be consistent within a contract surface.

#### DATA-14 — Boundary validation and safe errors

Requests shall be validated at the boundary. Errors shall be stable and actionable without exposing internal or sensitive details.

#### DATA-15 — Operational contract behavior

Contracts shall define applicable authentication, authorization, tenancy, rate limits, timeouts, retry behavior, and idempotency.

#### DATA-16 — Compatibility by default

Existing consumer contracts shall remain compatible unless a breaking change is explicitly authorized.

#### DATA-17 — Breaking-change lifecycle

A breaking contract change shall include appropriate versioning, migration guidance, a deprecation period, and a defined removal condition.

#### DATA-18 — Contract documentation

Public and materially shared APIs shall provide machine-readable contracts and useful examples where the protocol supports them.

#### DATA-19 — Contract verification

Important integration contracts shall be verified from provider and consumer perspectives where practical.

#### DATA-20 — Asynchronous semantics

Events, webhooks, queues, and asynchronous commands shall define delivery, ordering, duplication, retry, and failure semantics where they affect consumers.

#### DATA-21 — Integration diagnostics

Integrations shall provide enough diagnostic evidence to investigate failures without exposing sensitive payloads.

#### DATA-22 — Safe contract retirement

Obsolete contract versions shall be removed only after known consumers have migrated or the agreed support period has ended.

### Compatibility and deprecation

#### DATA-23 — Compatibility-surface inventory

Projects shall identify applicable compatibility surfaces, including public APIs, packages, CLI commands and exit codes, configuration, database and file formats, events, exports, URLs, extension storage, and mobile-client contracts.

#### DATA-24 — Preserve relied-upon behavior

Documented and materially relied-upon behavior shall remain compatible by default.

#### DATA-25 — Defined support window

Projects shall define the versions and upgrade paths they support rather than imply indefinite compatibility.

#### DATA-26 — Effective deprecation notice

Deprecations shall identify a replacement and removal condition and shall be communicated through channels visible to affected consumers.

#### DATA-27 — Configuration evolution

Configuration changes shall remain backward-compatible where practical. Invalid or obsolete settings shall produce actionable feedback rather than being silently ignored.

#### DATA-28 — Stable machine interfaces

Machine-consumed CLI output and exit semantics shall remain stable and shall be separable from human-oriented diagnostics.

#### DATA-29 — Persisted-state migration

Applications, mobile clients, and browser extensions shall migrate persisted state safely across supported versions.

#### DATA-30 — Version coexistence

Older deployed mobile apps, extensions, and rolling server versions shall be able to coexist with updated services for a defined support period.

#### DATA-31 — Upgrade-path verification

Releases shall verify upgrades from the oldest supported version and fresh installation of the new version where applicable.

#### DATA-32 — Data portability during retirement

When a product or storage format is retired, users shall retain access to exportable data in a useful format when applicable.

#### DATA-33 — Emergency compatibility breaks

An urgent compatibility break shall be permitted only when required for safety or security and shall include clear impact and migration guidance.

## 11. Performance and scalability

**Status:** Approved

### Performance requirements

#### PERF-1 — Workload-derived goals

Performance goals shall derive from actual users, workloads, devices, networks, data volumes, and operational constraints.

#### PERF-2 — No universal performance target

Projects shall not inherit universal latency or throughput numbers that are unrelated to their requirements.

#### PERF-3 — Measurable budgets

Durable projects shall define measurable budgets for applicable qualities such as response time, UI responsiveness, startup time, memory, CPU, battery, network use, bundle size, throughput, and cost.

#### PERF-4 — Baseline before optimization

Existing behavior shall be measured under representative conditions before performance optimization begins.

#### PERF-5 — Evidence-based optimization

Optimization shall address measured bottlenecks and favor the simplest change with material impact.

#### PERF-6 — Representative performance verification

Critical paths shall be tested with realistic data sizes, concurrency, and constrained client conditions where those factors matter.

#### PERF-7 — Regression protection

Material performance requirements shall have suitable regression detection.

#### PERF-8 — Tail behavior

Performance assessment shall include materially slow common behavior and shall not rely only on averages.

#### PERF-9 — Bounded efficiency

Systems shall use resources efficiently and predictably without adding scaling complexity for hypothetical demand.

#### PERF-10 — Quick-experiment scope

Quick experiments require performance work only when performance is the experiment's purpose or the solution cannot function acceptably without it.

### Scalability and capacity

#### PERF-11 — Capacity expectations

Systems for which scale matters shall define expected normal load, peak load, growth horizon, and acceptable operating limits.

#### PERF-12 — Simplest sufficient scaling

The architecture shall use the simplest scaling approach that meets demonstrated targets, including vertical scaling where sufficient.

#### PERF-13 — Evidence for distributed scaling

Horizontal distribution, partitioning, queues, caches, and specialized data stores shall require a demonstrated capacity or reliability need.

#### PERF-14 — Load verification

Important systems shall receive representative load testing before launches or changes expected to approach capacity limits.

#### PERF-15 — Capacity headroom

Production systems shall retain reasonable capacity headroom and detect saturation before it causes widespread user failure.

#### PERF-16 — Bounded work

Queries, collections, uploads, concurrency, retries, and queued work shall have limits appropriate to their risk and resource cost.

#### PERF-17 — Overload behavior

Systems shall apply backpressure or graceful load shedding when capacity is exhausted, preserving essential operations and degrading optional behavior safely where practical.

#### PERF-18 — Cache correctness

Cached data shall have defined freshness and invalidation behavior.

#### PERF-19 — Autoscaling limits

Autoscaling shall complement efficient behavior and explicit limits rather than replace them.

#### PERF-20 — Scaling economics

Scalability decisions shall account for infrastructure cost and operational complexity.

#### PERF-21 — Scaling triggers

Known capacity limits and the evidence that should trigger the next scaling step shall be documented when material.

## 12. Reliability, recovery, and operations

**Status:** Approved

### Reliability and failure handling

#### REL-1 — Critical-operation classification

Durable systems shall identify critical user and business operations and define their required availability, durability, and acceptable degradation.

#### REL-2 — Purposeful service objectives

Measurable service objectives shall be set when they provide operational value and shall derive from system requirements rather than a universal availability percentage.

#### REL-3 — Bounded waiting

Remote and potentially blocking operations shall have time limits appropriate to their expected behavior and impact.

#### REL-4 — Safe retries

Only failures likely to be transient shall be retried. Retry behavior shall be bounded and shall prevent unintended duplicate effects.

#### REL-5 — Failure isolation

A failing dependency, workload, or resource pool shall not be allowed to exhaust or cascade through the entire system where isolation is practical.

#### REL-6 — Graceful degradation

Optional behavior should degrade safely while preserving critical operations where practical.

#### REL-7 — Honest completion state

A system shall not report success when required work was lost or remains in an unknown state.

#### REL-8 — Repeatable recovery operations

Restarts, repeated messages, scheduled jobs, and recovery operations shall be safe to repeat where duplication is possible.

#### REL-9 — Health-state distinction

Operational health shall distinguish whether a process is alive, ready to receive work, and functioning sufficiently to serve its intended traffic.

#### REL-10 — Permanently failing work

Poisoned or permanently failing background work shall become visible for diagnosis and resolution rather than retry indefinitely.

#### REL-11 — Failure-path verification

Meaningful failure cases, including unavailable dependencies, partial responses, timeouts, resource exhaustion, and interrupted processing, shall be verified where applicable.

#### REL-12 — Proportionate resilience exercises

Fault-injection and recovery exercises shall be used when system risk and complexity justify their cost.

### Backup and disaster recovery

#### REL-13 — Recoverability classification

Projects shall identify which data and configuration must survive loss and which state can be recreated.

#### REL-14 — Recovery objectives

Recovery-point and recovery-time objectives shall derive from business impact where recovery matters.

#### REL-15 — Protected automated backups

Irreplaceable production data shall be backed up automatically. Backups shall be protected from unauthorized access, tampering, and the same failure domains as the primary system.

#### REL-16 — Retained recovery points

Backup retention shall provide multiple recovery points appropriate to data, operational, and applicable compliance needs.

#### REL-17 — Backup independence

Replication and high availability shall not be treated as substitutes for recoverable backups.

#### REL-18 — Restore verification

A backup shall not be considered reliable until restoration has been demonstrated. Restore tests shall occur at a frequency proportionate to system risk.

#### REL-19 — Pre-change recovery check

A recent recoverable backup shall be verified before destructive migrations or high-risk data operations.

#### REL-20 — Complete recovery scope

Recovery planning shall include the schemas, configuration, infrastructure definitions, encryption-key recovery, and operational dependencies required to restore service.

#### REL-21 — Controlled recovery access

Access to backups and restoration operations shall be restricted and auditable.

#### REL-22 — Recovery instructions and exercises

Systems requiring disaster recovery shall maintain concise recovery instructions and exercise them in proportion to risk.

#### REL-23 — Recovery outcome reporting

After an actual recovery, the achieved recovery time and any data loss shall be measured and reported.

#### REL-24 — Reproducible-system exemption

Reproducible tools and disposable systems may omit backups when they contain no irreplaceable state.

### Operational readiness

#### REL-25 — Operational ownership

Each durable production system shall have an accountable owner and an escalation path proportionate to its importance.

#### REL-26 — Operational inventory

Production systems shall maintain an accurate inventory of their environments, dependencies, data stores, scheduled work, external services, and operational endpoints.

#### REL-27 — Focused runbooks

Consequential or recurring operational procedures shall be documented. Applicable examples include deployment, rollback, restoration, credential rotation, certificate renewal, DNS changes, and capacity response.

#### REL-28 — Reproducible environments

Infrastructure and environment setup shall be reproducible to the extent required for reliable operation and recovery.

#### REL-29 — Configuration readiness

Required configuration shall be validated before a system accepts production work, with clear feedback for missing or invalid values.

#### REL-30 — Environment differences

Material differences among development, test, staging, and production shall be documented and intentional.

#### REL-31 — Lifecycle maintenance

Routine maintenance should be automated, and material expirations for certificates, domains, credentials, dependencies, and supported platforms shall be tracked.

#### REL-32 — Manual-change reconciliation

Emergency or manual production changes shall be recorded and reconciled with the maintained configuration afterward.

#### REL-33 — Readiness review

An operational-readiness check shall occur before the first production release and after material architectural changes.

#### REL-34 — Operator-safe tools

Commands and scripts used by operators shall provide clear help, meaningful exit status, and safe failure behavior.

#### REL-35 — Proportionate operational process

Systems shall not require on-call processes or extensive runbooks when their impact does not justify them.

### Incident management

#### REL-36 — Impact-based severity

Incident severity shall reflect user, data, security, financial, and operational impact.

#### REL-37 — Actionable alert ownership

Alerts shall represent conditions requiring action and shall identify an owner and enough context to begin diagnosis.

#### REL-38 — Proportionate response coverage

An on-call or equivalent response path shall be maintained only for systems whose required availability justifies it.

#### REL-39 — Incident priorities

Incident response shall prioritize safety, containment, service restoration, and clear status communication.

#### REL-40 — Evidence preservation

Useful incident evidence shall be preserved without unnecessary collection or disclosure of sensitive data.

#### REL-41 — Incident decision record

Significant decisions and production changes made during an incident shall be recorded.

#### REL-42 — Learning review

Material incidents and meaningful near misses shall receive a concise, blame-free review focused on contributing system and process conditions.

#### REL-43 — Corrective-action ownership

Corrective actions shall have an owner and priority and shall be tracked to completion.

#### REL-44 — Recurrence prevention

Tests, monitoring, automation, documentation, or safeguards shall be improved when doing so would prevent recurrence or shorten recovery.

#### REL-45 — Useful incident metrics

Detection and recovery times shall be measured when those measurements help improve operations.

#### REL-46 — Proportionate incident ceremony

Routine low-impact failures shall not require a formal incident process.

## 13. Observability and production logging

**Status:** Approved

### Observability baseline

#### OBS-1 — Structured production logs

Every durable production service shall emit structured, searchable logs.

#### OBS-2 — Common event context

Production log events shall include applicable UTC timestamp, severity, service, environment, release version, event name, and correlation context.

#### OBS-3 — Meaningful severity

Log levels shall be used consistently. Error severity shall represent failed requested work or conditions requiring investigation.

#### OBS-4 — Diagnostic but data-safe context

Logs shall contain enough context to diagnose behavior without including secrets, credentials, session tokens, or unnecessary personal data.

#### OBS-5 — Operational metrics

Production services shall collect applicable metrics for traffic, errors, latency, resource saturation, queue health, and critical business outcomes.

#### OBS-6 — Purposeful tracing

Distributed tracing shall be added when requests cross multiple meaningful boundaries and logs alone cannot adequately explain latency or failure.

#### OBS-7 — Decision-oriented dashboards

Dashboards shall focus on user impact, service objectives, capacity, and operational decisions rather than metrics without an intended use.

#### OBS-8 — Actionable alerts

Alerts shall represent actionable symptoms or imminent capacity risks and shall have an expected response.

#### OBS-9 — Developer and CLI output

Local tools and development workflows shall provide concise human-readable output, with detailed diagnostics available on demand.

#### OBS-10 — Quick experiments

Quick experiments require no observability unless it is needed to solve or evaluate the experiment.

#### OBS-11 — Proportionate instrumentation

Small standalone tools shall not require metrics or tracing when those signals provide no operational value.

### Log destination and format

#### OBS-12 — Platform-managed service logging

Containerized and platform-managed services shall write logs to standard streams and rely on the runtime or logging platform for collection, rotation, and retention.

#### OBS-13 — Standalone file logging

Standalone host services may write rotating files when a reliable platform collector is unavailable.

#### OBS-14 — Structured production format

Machine-consumed production logs shall use structured JSON or the established structured format of the project's logging platform.

#### OBS-15 — Readable development format

Local development shall default to readable console output while preserving the event information available in production.

#### OBS-16 — Separated CLI diagnostics

CLI tools shall keep normal machine-consumable output stable and shall provide diagnostics through a distinct channel.

#### OBS-17 — Bounded client diagnostics

Desktop, mobile, and browser-extension logs shall use bounded local diagnostic storage and shall support deliberate export when troubleshooting requires it.

#### OBS-18 — Separate security audit records

Security audit records shall be separated from ordinary diagnostic logs when their integrity, access, or retention requirements differ.

#### OBS-19 — Configurable log level

Log level shall be configurable by environment, with targeted production diagnostics available without rebuilding the software.

#### OBS-20 — Temporary production debugging

Elevated production debug logging shall expire or be deliberately disabled after its troubleshooting purpose ends.

### Log rotation and retention defaults

#### OBS-21 — Centralized production retention

Centralized production diagnostic logs shall remain searchable for 90 days by default.

#### OBS-22 — Standalone production rotation

Standalone production log files shall rotate when they reach 100 MiB or 24 hours of age, whichever occurs first. Rotated files shall be compressed and retained for 90 days by default.

#### OBS-23 — Standalone storage cap

Standalone production logs shall have a default total cap of 5 GiB per service. The oldest eligible diagnostic logs shall be removed before log storage exhaustion.

#### OBS-24 — Retention shortfall visibility

When a storage cap prevents production logs from reaching their time-based retention target, the shortfall shall be surfaced operationally.

#### OBS-25 — Security audit retention

Security audit records shall be retained for 90 days by default.

#### OBS-26 — Development retention

Local development logs shall have a default retention of 7 days and a total cap of 500 MiB per project.

#### OBS-27 — End-user device retention

Mobile, desktop, and browser-extension diagnostic logs shall have a default retention of 7 days and a local cap of 10 MiB per application.

#### OBS-28 — Configurable and validated limits

Log level, retention period, per-file size, and total storage limits shall be configurable and validated before production work begins.

#### OBS-29 — Requirement-specific overrides

Legal, privacy, contractual, operational, and storage requirements may override the default logging limits.

#### OBS-30 — Lifecycle verification

Rotation, compression, retention, and deletion behavior shall be verified rather than assumed from configuration.

### Logged event coverage

#### OBS-31 — Lifecycle events

Durable applications shall log startup and shutdown with applicable environment identity and release version.

#### OBS-32 — Configuration validation events

Configuration validation outcomes shall be logged without exposing sensitive configuration values.

#### OBS-33 — Operation completion events

Material requests and operations shall record their outcome, duration, and correlation identifier where applicable.

#### OBS-34 — Diagnostic error events

Errors shall identify the failed operation, include relevant safe context, preserve the underlying cause, and provide stack information when useful.

#### OBS-35 — Dependency failure events

External dependency failures, timeouts, and material latency effects shall be recorded with safe diagnostic context.

#### OBS-36 — Background-work events

Material background work shall record applicable start, completion, retry, and terminal-failure events.

#### OBS-37 — Security event coverage

Authentication events, authorization denials, privilege changes, administrative actions, and other security-relevant events shall be recorded according to their audit needs.

#### OBS-38 — Auditable data changes

Material data changes shall be recorded when accountability, investigation, or applicable obligations require an audit trail.

#### OBS-39 — No payload logging by default

Full request and response bodies shall not be logged by default.

#### OBS-40 — Useful event selection

Routine high-volume events that provide no diagnostic or operational value shall be omitted.

#### OBS-41 — Safe sampling

Sampling may reduce eligible high-volume diagnostics but shall not discard errors, required security audit records, or compliance-required events.

#### OBS-42 — Correlation propagation

Correlation context shall be propagated across requests, background work, and integrations where practical.

### Metrics, traces, and alerts

#### OBS-43 — Operational metric coverage

Production services shall measure applicable traffic, errors, latency, and saturation, together with a small set of critical business outcomes.

#### OBS-44 — Stable metric definitions

Metric names, units, and labels shall remain stable and documented where they are operationally relied upon.

#### OBS-45 — Bounded metric cardinality

Metrics shall not use unbounded label values such as user identifiers, request identifiers, raw URLs, or arbitrary error text.

#### OBS-46 — Metric retention defaults

Full-resolution production metrics shall be retained for 30 days and aggregated production metrics for 13 months by default.

#### OBS-47 — Purposeful trace coverage

Cross-boundary operations shall be traced when traces materially improve diagnosis of latency or failure.

#### OBS-48 — Trace retention defaults

Ordinary sampled traces shall be retained for 7 days and failed or designated high-value traces for 30 days by default.

#### OBS-49 — Telemetry data safety

Sensitive data shall not be placed in metric labels or trace attributes.

#### OBS-50 — Alert-worthy conditions

Alerts shall focus on user-visible failure, service-objective risk, security conditions requiring response, and approaching resource exhaustion.

#### OBS-51 — Actionable alert definition

Every alert shall identify an owner, severity, actionable context, and response guidance.

#### OBS-52 — Alert noise control

Related alerts shall be deduplicated and expected noise shall be suppressed during controlled maintenance.

#### OBS-53 — Alert-path verification

Critical alerts shall be tested to verify that they fire and reach the intended destination.

#### OBS-54 — Reviewable observability configuration

Dashboards, alert definitions, and material instrumentation changes shall remain reviewable with the software.

#### OBS-55 — Retention overrides

Project risk, troubleshooting needs, privacy requirements, and storage cost may override metric and trace retention defaults.

## 14. User experience and accessibility

**Status:** Approved

### Accessibility baseline

#### UX-1 — Durable interface accessibility

Durable user interfaces, including internal tools, shall support their primary tasks clearly, consistently, and efficiently.

#### UX-2 — Accessibility target

Web interfaces shall meet WCAG 2.2 Level AA. Native and hybrid mobile applications shall meet equivalent applicable platform accessibility guidance.

#### UX-3 — Semantic and operable controls

Interfaces shall use meaningful semantics and labels, logical reading and focus order, and complete keyboard operation where the platform supports a keyboard.

#### UX-4 — Accessible perception and motion

Interfaces shall support applicable screen readers, text resizing, sufficient contrast, visible focus, reduced motion, and alternatives to meaning conveyed only by color or sound.

#### UX-5 — Input-method accessibility

Touch targets and interactions shall remain usable across supported devices and input methods.

#### UX-6 — Complete interaction states

Applicable loading, empty, success, validation, error, offline, and permission-denied states shall be clear and usable.

#### UX-7 — Data-loss prevention

Interfaces shall prevent accidental data loss. Destructive actions shall be confirmed or reversible according to their impact.

#### UX-8 — Accessibility across variants

Accessibility shall remain intact across responsive layouts, localization, and dynamic updates.

#### UX-9 — Accessibility verification

Critical flows shall receive automated accessibility checks together with appropriate keyboard and assistive-technology verification.

#### UX-10 — Accessibility regressions

Accessibility regressions shall be treated as defects rather than optional polish.

#### UX-11 — Quick-experiment accessibility

Quick experiments may omit formal accessibility verification but should retain accessible platform defaults when doing so adds negligible effort.

### Task-first user experience

#### UX-12 — Function before visual style

User experience and functional efficiency shall take priority over decorative visual styling.

#### UX-13 — Minimal task steps

Common tasks shall require the fewest clear interactions and context changes consistent with safety and comprehension.

#### UX-14 — Direct completion flow

When a task can be understood and completed in one context, the interface should let the user provide the required input, perform the action, and see the result without unnecessary pages, dialogs, or confirmation steps.

#### UX-15 — Styling serves usability

Visual design shall support hierarchy, readability, state recognition, and action discovery rather than introduce ceremony or distract from the task.

#### UX-16 — Justified multi-step flows

A task shall use multiple steps only when doing so materially reduces complexity or risk, supports conditional input, enables save-and-resume behavior, satisfies a required disclosure or consent, or provides necessary review for a high-impact action.

#### UX-17 — Multi-step continuity

When multiple steps are justified, the interface shall show progress, preserve entered data, allow safe backward navigation, and present a final summary when useful.

#### UX-18 — Progressive disclosure

Rare and advanced options should remain available through progressive disclosure rather than adding steps or complexity for every user.

### Forms and action feedback

#### UX-19 — Minimal required input

Forms shall request only information required to complete the task and should derive or default values when doing so is reliable.

#### UX-20 — Visible sensible defaults

Defaults shall be sensible, visible, and easy to change.

#### UX-21 — Actionable validation

Validation shall appear near the relevant input and explain how to correct the problem.

#### UX-22 — Preserve valid input

Valid user input shall not be erased when validation or submission fails.

#### UX-23 — Accessible error navigation

Forms shall direct attention to the first relevant error and shall provide an understandable error summary when form complexity warrants one.

#### UX-24 — Standard input capabilities

Forms shall support applicable paste, autofill, password-manager, keyboard-submission, and native input behavior.

#### UX-25 — Timely action feedback

An interface shall acknowledge an action promptly and shall show meaningful progress when completion takes noticeable time.

#### UX-26 — Duplicate-action protection

Interfaces shall prevent accidental duplicate submission while preserving a safe path to retry failed work.

#### UX-27 — Contextual results

Results should appear in the same working context unless a separate view materially improves the task.

#### UX-28 — Valuable draft preservation

Lengthy or valuable user input shall be preserved as a draft when loss would impose meaningful rework.

#### UX-29 — Explained unavailability

When an action is unavailable, the interface shall make the reason and required next step understandable.

#### UX-30 — Honest interaction design

Interfaces shall avoid surprise navigation, hidden requirements, manipulative choices, and unnecessary confirmations.

### Visual design

#### UX-31 — Existing design language

Interfaces shall follow the project's existing design system and platform conventions when they are sound.

#### UX-32 — Restrained new design

New products shall use a simple, restrained visual system with clear hierarchy, readable typography, consistent spacing, and recognizable controls.

#### UX-33 — Familiar controls

Standard or platform-native controls shall be preferred unless a custom control provides a material usability benefit.

#### UX-34 — Task-appropriate density

Information density shall reflect the task and input method, including compact presentation for frequent data-heavy work and sufficient space for touch and occasional use.

#### UX-35 — Supported responsive layouts

Interfaces shall support required screen sizes without hiding critical actions or introducing avoidable horizontal scrolling.

#### UX-36 — Purposeful motion

Animation shall be used only when it clarifies state, feedback, or spatial change.

#### UX-37 — Consistent interaction language

Components, behavior, and terminology shall remain consistent throughout a product.

#### UX-38 — Proportionate polish

Visual polish shall make state and actions clear without delaying working functionality for decorative refinement.

#### UX-39 — Visual verification

Critical screens and states shall be visually verified across supported layouts before completion.

### CLI and script usability

#### UX-40 — Efficient common command

The common operation shall require the fewest arguments and configuration steps consistent with clarity and safety.

#### UX-41 — Discoverable command usage

Command-line tools shall provide concise help, realistic examples, and version information.

#### UX-42 — Consistent command language

Command names, flags, defaults, and argument behavior shall remain consistent within a tool.

#### UX-43 — Predictable configuration precedence

Precedence among command-line arguments, environment settings, and configuration files shall be defined and predictable.

#### UX-44 — Non-interactive operation

Tools intended for automation shall support non-interactive use without prompts when all required inputs are supplied.

#### UX-45 — Automation-safe output

Result output shall remain distinct from diagnostics, and a stable machine-readable format shall be available when automation is expected.

#### UX-46 — Meaningful exit status

Command-line tools and scripts shall return exit codes that accurately distinguish success from relevant failure classes.

#### UX-47 — Destructive command intent

Destructive interactive operations shall require deliberate confirmation. Unattended destructive execution shall require an explicit override.

#### UX-48 — Impact preview

Impactful bulk operations shall provide a preview or dry-run mode when practical.

#### UX-49 — Secret-safe input

Secrets shall not be requested through channels likely to retain them in shell history or process listings when a safer practical channel exists.

#### UX-50 — Output-safe progress

Progress output shall appear only when useful and shall not corrupt piped or machine-readable output.

#### UX-51 — Safe interruption

Interruption shall not leave data in a corrupted or misleading state.

#### UX-52 — Adjustable verbosity

Quiet and verbose modes shall be available when different output levels serve real use cases.

### Mobile and browser-extension experience

#### UX-53 — Platform conventions

Mobile applications and browser extensions shall follow applicable platform conventions for navigation, back behavior, lifecycle, settings, and system integration.

#### UX-54 — Contextual permission requests

Permissions shall be requested when their related feature is used, with a clear explanation of the benefit. Denial of an optional permission shall leave unrelated behavior usable.

#### UX-55 — State preservation

Valuable user state shall survive applicable suspension, process termination, browser closure, and application updates.

#### UX-56 — Connectivity state

Offline, reconnecting, synchronized, and stale-data states shall be understandable to the user.

#### UX-57 — Safe offline actions

Offline actions shall be queued only when they can be replayed safely. Otherwise, the interface shall explain why connectivity is required.

#### UX-58 — Conflict-safe synchronization

Synchronization conflicts shall not silently overwrite user work.

#### UX-59 — Constrained-network usability

Supported workflows shall account for slow and intermittent networks where those conditions are realistic.

#### UX-60 — Appropriate extension context

Short extension interactions shall remain concise, while workflows that do not fit safely in a small extension surface shall use an appropriate larger context.

#### UX-61 — Contextual links and notifications

Deep links and notifications shall lead to the relevant context while preserving required authentication and authorization checks.

#### UX-62 — Update-safe user state

Application updates and stored-state migrations shall preserve user settings and work.

#### UX-63 — Device resource awareness

Mobile and extension behavior shall respect applicable battery, bandwidth, storage, and background-execution constraints.

### Localization and regional behavior

#### UX-64 — Requirements-driven localization

Full localization support shall be required only when the intended audience or credible roadmap requires multiple languages.

#### UX-65 — Region-safe data handling

Products shall handle applicable Unicode, names, addresses, dates, time zones, numbers, and currencies without unsafe regional assumptions, even when the interface supports one language.

#### UX-66 — Translatable interface behavior

Localized products shall support translatable user-facing text, text expansion, pluralization, and right-to-left layout where applicable.

#### UX-67 — Locale-aware presentation

Dates, times, numbers, and currencies shall follow the user's selected locale while preserving an unambiguous underlying value.

#### UX-68 — Explicit time-zone meaning

Scheduled and historical events shall make their time-zone meaning clear where ambiguity could affect users.

#### UX-69 — Translation fallback

Localized products shall provide a predictable fallback for unavailable translations and shall detect missing translations before release.

#### UX-70 — Critical translation review

Important legal, safety, financial, and security text shall receive competent human review rather than rely solely on machine translation.

#### UX-71 — User-content preservation

User-created content shall be preserved accurately across locales.

#### UX-72 — Proportionate localization infrastructure

Single-language internal tools shall not require a complete localization system unless expansion is reasonably expected.

## 15. Documentation and knowledge preservation

**Status:** Approved

### Documentation baseline

#### DOC-1 — Durable project entry document

Every durable project shall have a concise entry document covering its purpose, intended users, prerequisites, setup, configuration, common commands, testing, and how to run it.

#### DOC-2 — Material documentation scope

Public contracts, operator-required behavior, non-obvious constraints, and consequential decisions shall be documented.

#### DOC-3 — Avoid implementation duplication

Routine implementation details shall remain in clear code and tests rather than be duplicated in prose.

#### DOC-4 — Intent-focused comments

Code comments shall explain intent, tradeoffs, hazards, and external constraints rather than restate what the code does.

#### DOC-5 — Documentation changes with behavior

Affected documentation shall be updated in the same change as related behavior, configuration, or workflow changes.

#### DOC-6 — Discoverable documentation

Documentation should remain close to the source it describes where practical and shall provide a clear starting point for readers.

#### DOC-7 — Generated reference with human guidance

Machine-defined contracts should generate their reference material where practical, supplemented by human guidance and realistic examples.

#### DOC-8 — Verified instructions

Documented commands and examples shall be verified sufficiently to avoid giving users stale or invalid instructions.

#### DOC-9 — Obsolete documentation removal

Obsolete documentation shall be corrected or removed rather than retained alongside conflicting guidance.

#### DOC-10 — Documentation with a reader

Documentation shall be required only when it has an identifiable reader and continuing maintenance value.

#### DOC-11 — Quick-experiment documentation

Quick experiments require only the documentation necessary to run or evaluate them.

### Cross-session knowledge preservation

#### DOC-12 — Reusable personal baseline

Personal defaults shall live in one reusable, version-controlled baseline rather than be copied in full into every project.

#### DOC-13 — Concise project instructions

Each durable repository shall provide concise project instructions that link to or are combined with the personal baseline.

#### DOC-14 — Project knowledge scope

Project instructions shall record the architecture map, authoritative commands, conventions, supported environments, important constraints, deployment and verification expectations, and known hazards that apply to future work.

#### DOC-15 — Instruction precedence

Requirements shall follow this precedence: the user's current instruction, project-specific requirements, and then personal defaults.

#### DOC-16 — Read instructions before work

The agent shall read applicable project instructions before planning or editing.

#### DOC-17 — Durable source of truth

Consequential decisions and established facts shall be preserved in maintained project documents. Chat history and session summaries shall not be their sole source of truth.

#### DOC-18 — Knowledge updates

When work introduces or discovers a durable constraint, command, integration, or operational requirement, the applicable project knowledge shall be updated.

#### DOC-19 — Separate temporary progress

Temporary progress notes shall remain separate from stable project guidance.

#### DOC-20 — No secrets in instructions

Credentials and sensitive operational values shall not be stored in agent-memory or instruction files.

#### DOC-21 — Remove stale guidance

Instructions that no longer describe the project shall be corrected or removed.

#### DOC-22 — Project-specific content

Repository instructions shall avoid repeating generic coding guidance and shall focus on project-specific differences and references to the shared baseline.

## 16. Verification, completion, and reporting

**Status:** Approved

### Definition of done

#### DONE-1 — Accepted behavior

The requested behavior and every agreed acceptance criterion shall be satisfied before a task is complete.

#### DONE-2 — Required checks

Applicable automated tests, formatting, linting, type checks, builds, security checks, migration checks, and platform checks shall pass.

#### DONE-3 — Behavioral evidence

New and changed behavior shall have meaningful verification evidence.

#### DONE-4 — Final diff review

The agent shall review the final diff for correctness, simplicity, unintended changes, and missing edge cases.

#### DONE-5 — Supporting artifacts

Required documentation, configuration, migrations, release notes, and operational material shall be updated with the change.

#### DONE-6 — No unresolved in-scope defect

A task shall not be complete while a known unresolved defect remains within its scope unless the user explicitly accepts it.

#### DONE-7 — Deployment completion

When deployment is part of the task, completion shall require successful deployment and health verification.

#### DONE-8 — Git completion

All task changes shall be committed, an upstream push shall be attempted when configured, and the applicable pull-request policy shall be followed.

#### DONE-9 — Preserve unrelated work

Existing unrelated user work shall remain intact.

#### DONE-10 — Complete final report

The final report shall state what changed, what was verified, commit and push status, deployment status when applicable, and any remaining limitations or unrelated findings.

#### DONE-11 — Honest incomplete status

A task shall not be reported as complete when a required check failed or could not run. The report shall identify what remains and why.

### Verification depth

#### DONE-12 — Fast implementation feedback

The smallest relevant checks shall run during implementation to provide fast feedback.

#### DONE-13 — Affected pre-completion checks

Before completion, the full set of checks affected by the change and all repository-required gates shall pass.

#### DONE-14 — Full-suite triggers

The entire project suite shall run when a change is broad, cross-cutting, release-critical, or subject to a repository requirement for full verification.

#### DONE-15 — Environment-independent evidence

Verification shall use a clean or reproducible environment when existing environment state could conceal a defect.

#### DONE-16 — Success and failure paths

Verification shall cover the successful behavior and important failure, boundary, permission, and recovery paths applicable to the change.

#### DONE-17 — Real behavior inspection

User-facing and integration behavior shall be exercised directly when automated checks cannot establish the real outcome.

#### DONE-18 — Resulting external state

For external systems, verification shall inspect the resulting state rather than rely solely on a successful command response.

#### DONE-19 — Artifact verification

Migrations, generated artifacts, configuration, and deployment manifests shall be compared with their intended results where applicable.

#### DONE-20 — Exact check reporting

The final report shall identify the checks run and their outcomes.

#### DONE-21 — No inferred pass claims

A check shall not be reported as passing when it was skipped, unavailable, or merely inferred.

#### DONE-22 — Verification-gap disclosure

When full verification is impractical, the specific gap, resulting risk, and best available evidence shall be reported.

### Completion reporting

#### DONE-23 — Outcome-first report

Completion reports shall lead with the achieved outcome and resulting behavior.

#### DONE-24 — Material change summary

Reports shall summarize material changes and reference the most relevant files rather than enumerate every edited file.

#### DONE-25 — Verification results

Reports shall state the verification performed and the outcome of each relevant check.

#### DONE-26 — Git and review status

Applicable branch, commit, push result, and pull-request location shall be reported.

#### DONE-27 — Deployment result

When deployment is included, the report shall identify the environment, release, and health result.

#### DONE-28 — Fact and inference distinction

Verified facts shall be distinguishable from assumptions and inferred conclusions.

#### DONE-29 — Useful decision context

Material design decisions shall be reported only when they help review or future maintenance.

#### DONE-30 — Remaining concerns

Remaining limitations, accepted risks, verification gaps, and unrelated findings shall be stated clearly.

#### DONE-31 — Necessary user actions

The report shall request user action only when something genuinely remains for the user to do.

#### DONE-32 — Proportionate report detail

Completion reports shall be brief for small changes and structured in proportion to complex work.

#### DONE-33 — No work diary

Completion reports shall omit routine tool narration, raw logs, and chronological work diaries.

## 17. Framework evaluation and continuous improvement

**Status:** Approved

### Anti-bloat framework design

#### FRAME-1 — Small mandatory core

The mandatory workflow core shall be limited to understanding the requirement, clarifying material ambiguity, presenting a plan only when the agent must choose a material approach, implementing, verifying, committing, and reporting.

#### FRAME-2 — Applicability-driven controls

Requirements outside the core shall activate only when the project type, requested change, risk, or explicit configuration makes them applicable.

#### FRAME-3 — Explicit project profiles

The durable profile shall be the default. The quick-experiment profile shall require an explicit user override.

#### FRAME-4 — Outcome and boundary rules

Shared rules shall express required outcomes and decision boundaries rather than lengthy procedural scripts.

#### FRAME-5 — Local technology guidance

Language, framework, and repository-specific guidance shall remain in project-level instructions rather than expand the shared baseline.

#### FRAME-6 — No mandatory ceremony

The framework shall not require brainstorming rituals, repeated plan documents, persona scripts, fixed phase announcements, or reviewer agents without a concrete need.

#### FRAME-7 — No repeated checklist narration

The same checklist shall not be repeated across prompts, plans, implementation notes, and completion reports.

#### FRAME-8 — Inapplicable-control omission

The agent may omit clearly inapplicable controls without asking but shall address every applicable material control.

#### FRAME-9 — Proportionate effort

Planning, testing, documentation, and reporting effort shall scale with the size and risk of the work.

#### FRAME-10 — Authoritative preference source

Each preference shall have one authoritative version referenced by profiles and projects.

#### FRAME-11 — Remove low-value rules

Rules that repeatedly add work without preventing meaningful mistakes or improving outcomes shall be removed or simplified.

### Framework evolution

#### FRAME-12 — Versioned baseline

The shared baseline shall be versioned and shall maintain a concise record of material preference changes.

#### FRAME-13 — User-controlled preference changes

The agent may propose baseline improvements but shall not change personal preferences silently.

#### FRAME-14 — Evidence threshold for new rules

A new shared rule shall address a recurring failure, a high-impact one-time failure, or a clearly established requirement.

#### FRAME-15 — Representative framework evaluation

Substantial framework changes shall be evaluated against representative small fixes, features, refactors, incidents, and quick experiments before broad adoption.

#### FRAME-16 — Outcome-based evaluation

Framework success shall be evaluated using missed requirements, unnecessary clarification, rework, escaped defects, delivery time, and maintenance burden.

#### FRAME-17 — Framework cost indicators

Prompt size, token use, document count, and agent-step count shall be treated as costs rather than evidence of quality.

#### FRAME-18 — Evidence-triggered review

The framework shall be reviewed when repeated friction or omissions appear rather than through heavy scheduled governance.

#### FRAME-19 — Preference maintenance

Framework reviews shall merge duplicate rules, resolve contradictions, and remove obsolete preferences.

#### FRAME-20 — Local exceptions

Justified project exceptions shall remain local with their reason rather than weaken the global default.

#### FRAME-21 — Agent portability

Requirements shall remain portable across Codex, Claude, and future agents. Tool-specific adapters shall preserve the same underlying preferences.

#### FRAME-22 — Project workflow continuity

Baseline changes that materially alter an existing project's workflow shall preserve compatibility unless the user explicitly migrates that project.

### Profile activation

#### FRAME-23 — Quick-mode command

The exact command `mode: quick` shall activate the quick-experiment profile for the task that follows and its related follow-up work.

#### FRAME-24 — Quick-mode scope

Quick mode shall end when its task is complete. A new unrelated task shall return to the durable profile automatically.

#### FRAME-25 — Durable default and override

The durable profile shall require no command. The command `mode: durable` may explicitly override a project or session profile when needed.

#### FRAME-26 — Unambiguous activation

Phrases that merely request speed shall not activate quick mode. The exact command or an unmistakable instruction that the work is a quick experiment shall be required.

#### FRAME-27 — Quick-mode disclosure

The completion report shall state when quick mode was used and shall identify material durable-software controls intentionally omitted.

#### FRAME-28 — Quick-mode safeguards

Quick mode may omit planning approval, TDD, broad testing, production observability, CI/CD, production architecture, durable documentation, compatibility work, and operational hardening when they are not needed for the experiment. It shall still protect secrets, user data, existing work, and authorization boundaries.

#### FRAME-29 — Durable promotion

A quick experiment shall not be treated as maintained or production-ready software until it is explicitly promoted to the durable profile and satisfies the applicable durable requirements.

### Delegation configuration

#### FRAME-30 — Delegation setting

The portable setting `delegation: false` or `delegation: true` shall control whether subagents may be used.

#### FRAME-31 — Disabled by default

The global default shall be `delegation: false`, which strictly prohibits subagent use.

#### FRAME-32 — Project delegation setting

A project may set `delegation: true` in its instructions to permit justified delegation for that project.

#### FRAME-33 — Task delegation override

A task prompt may set `delegation: true` or `delegation: false` to override the project setting for that task and its related follow-up work.

#### FRAME-34 — Delegation override scope

A task-level delegation override shall end when the task is complete.

#### FRAME-35 — Permission rather than mandate

The value `delegation: true` shall permit delegation only when it materially helps and shall not require subagents.

#### FRAME-36 — Delegation concurrency

Enabled delegation shall retain the default maximum of three concurrent subagents unless the user explicitly changes it.

#### FRAME-37 — Delegation precedence

The effective delegation setting shall follow this order: task setting, project setting, then global default.

## Unresolved decisions

None.
