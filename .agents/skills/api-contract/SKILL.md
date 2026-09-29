---
name: api-contract
description: Design or change durable APIs, events, webhooks, commands, schemas, or third-party integration contracts when consumer behavior and compatibility must be explicit.
---

# API and Integration Contracts

Create the smallest contract that expresses the consumer's use case and remains diagnosable and evolvable.

## Workflow

1. Identify consumers, use cases, trust boundaries, current contracts, supported versions, and failure expectations.
2. Reuse the project's established protocol and conventions when sound. Define names, types, validation, outcomes, errors, authorization, tenancy, and operational limits.
3. Preserve compatibility by default. If a breaking change is needed, make versioning, migration, deprecation, and removal conditions part of the approved scope.
4. For asynchronous behavior, define delivery, ordering, duplication, retry, idempotency, and terminal failure semantics.
5. Express public or materially shared contracts in a machine-readable form when the protocol supports it and include examples that clarify real use.
6. Test provider behavior and material consumer assumptions at the lowest sufficient level. Do not mock away the contract boundary being verified.

Read [contract review points](references/contract-review.md) when designing a new public surface or changing compatibility-sensitive behavior.
