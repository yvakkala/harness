# Security Review Reference

## Identity and access

- Use risk-proportionate authentication, with MFA for privileged users and sensitive operations.
- Enforce every protected action and resource at a trusted service boundary.
- Keep recovery no weaker than normal authentication and make sessions bounded and revocable.
- Separate administrative access and record security-relevant identity and privilege events without authenticators.

## Secrets and data

- Keep secrets out of source, history, logs, errors, fixtures, artifacts, screenshots, and distributed clients.
- Separate secrets by service and environment; support rotation and revocation.
- Minimize sensitive data, define ownership and retention, protect it across transit, storage, backups, exports, and deletion.
- Enforce user and tenant isolation at every applicable access path.

## Exposure and supply chain

- Expose only required services, endpoints, origins, permissions, and capabilities.
- Disable development modes and unsafe diagnostics in production; use least-privileged runtime identities.
- Lock dependencies, verify provenance and licensing, inspect privileged install behavior, and scan relevant source, dependencies, infrastructure, containers, secrets, and artifacts.
- Treat clients as untrusted and request only necessary mobile or extension permissions.

## Verification and response

- Add a regression test or durable control for a fixed vulnerability and check for the same root cause elsewhere.
- For destructive or effectively irreversible security changes, present exact impact and recovery before approval.
- Treat exposed credentials as compromised and rotate or revoke them; history rewriting requires separate authorization.
