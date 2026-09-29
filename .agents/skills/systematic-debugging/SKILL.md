---
name: systematic-debugging
description: Diagnose a reproducible bug, failing test, build failure, integration failure, performance regression, or unexpected technical behavior when the cause is not already established. Use evidence before proposing a fix.
---

# Systematic Debugging

Find and fix the earliest actionable cause without accumulating guesses or unrelated changes.

## Evidence loop

1. Read the complete failure, stack, exit status, environment, and recent relevant changes.
2. Reproduce the smallest representative failure. If reproduction is intermittent, collect the variables that differ rather than guessing.
3. Trace the bad state or behavior backward across calls and component boundaries until its first incorrect origin is identified.
4. Find a nearby working example or authoritative contract and compare assumptions, inputs, configuration, and dependencies.
5. State one falsifiable hypothesis and the evidence supporting it.
6. Test that hypothesis with the smallest safe observation or change. Change one meaningful variable at a time.
7. Once the cause is established, create a failing regression test when meaningful, implement the smallest complete correction, and verify the original symptom plus affected checks.

Use safe diagnostics: log whether a secret or configuration value is present and valid, never its contents. Remove temporary instrumentation that has no continuing operational value.

## Stop conditions

- Do not stack speculative fixes or change tests merely to hide the failure.
- If a hypothesis fails, incorporate the new evidence before the second distinct attempt.
- After two reasonable attempts fail for the same blocking condition, stop and ask the user with reproduction evidence, both attempts, the suspected cause, and the decision or access needed.
- If evidence shows a material architectural change is required, present it as a changed approach rather than smuggling it into a defect fix.

This skill adapts the evidence-first method from Superpowers. See [provenance and local differences](references/provenance.md).
