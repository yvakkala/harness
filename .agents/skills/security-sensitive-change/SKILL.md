---
name: security-sensitive-change
description: Implement or materially change authentication, authorization, payments, secrets, sensitive data, cryptography, public exposure, privileged operations, tenant isolation, or infrastructure security. Do not invoke for routine code changes without a real security boundary.
---

# Security-Sensitive Change

Make the security boundary and its evidence explicit without expanding ordinary work into a generic audit.

## Workflow

1. Identify protected assets, actors, trust boundaries, entry points, abuse cases, exposure, and impact. Use a lightweight assessment unless the system's risk warrants a formal threat model.
2. Establish concrete security acceptance criteria alongside functional behavior.
3. Prefer mature identity, cryptography, secret, and security-control implementations. Enforce authorization and validation at a trusted boundary with least privilege and deny-by-default behavior.
4. Address the complete lifecycle, including enrollment or provisioning, recovery, rotation, revocation, deletion, and incident response where applicable.
5. Test allowed and denied behavior, resource and tenant isolation, invalid inputs, replay or duplicate behavior, sensitive failure paths, and relevant logging redaction.
6. Run risk-appropriate security checks and validate findings by exploitability, exposure, and impact.
7. Block deployment for an unresolved exploitable critical or high-risk vulnerability unless an accountable owner records an accepted risk and expiry.

Read [the security review reference](references/review.md) for high-impact or internet-facing changes. Preserve user-approved functionality and explain any compatibility or operational consequence before implementation when it is material.
