---
name: infrastructure-change
description: Change durable Docker, host, DNS, TLS, reverse-proxy, firewall, service, or environment infrastructure where rollout and recovery must be explicit.
---

# Infrastructure Change

Preserve access, security, and recoverability while changing the environment that runs software.

## Workflow

1. Inspect the current topology, authoritative configuration, provider state, dependency order, access path, and rollback mechanism.
2. Establish the intended external behavior, affected environments, maintenance constraints, propagation delay, and success signals.
3. Present a proportional plan for changes that can interrupt service, alter exposure, rotate identity, change routing, or lock out operators.
4. Read [the infrastructure review](references/review.md) and apply only the relevant controls.
5. Prefer declarative, reviewable, repeatable configuration. Keep secrets and environment-specific values in protected configuration channels.
6. Validate syntax and policy before applying. Stage changes to preserve a working management path and minimize simultaneous variables.
7. Inspect resulting DNS, certificates, listening services, routes, firewall policy, health, logs, and externally observable behavior.
8. Roll back or use the established forward-recovery path when health or access checks fail.

Do not treat a successful command as proof that infrastructure reached the intended state. Never weaken exposure or access controls merely to make a deployment pass.
