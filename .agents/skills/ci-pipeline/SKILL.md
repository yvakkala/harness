---
name: ci-pipeline
description: Create or materially change durable CI workflows, build pipelines, caches, artifacts, security checks, or deployment triggers.
---

# CI Pipeline

Make automated validation reproducible, least-privileged, fast enough to use, and honest about failures.

## Workflow

1. Inspect existing workflows, repository protections, supported environments, local authoritative commands, secret boundaries, and deployment triggers.
2. Define the events, required checks, permissions, dependency inputs, artifacts, concurrency, and failure evidence needed for this repository.
3. Present a plan when changing trust boundaries, protected checks, release artifacts, or automatic deployment behavior. Disclose any push or merge that will deploy.
4. Read [the pipeline review](references/review.md) for workflows that consume secrets, build releases, or execute untrusted contributions.
5. Reuse the same committed commands and locked dependencies used locally. Pin external workflow dependencies to reviewed immutable revisions when practical.
6. Give workflow tokens and jobs the minimum permissions, credentials, network access, and artifact access they require.
7. Keep required failures blocking. Cache only safe reproducible inputs, use bounded retention, cancel superseded work where appropriate, and prevent incompatible deployments from racing.
8. Validate workflow syntax and exercise the closest safe event path. Confirm required checks, artifacts, diagnostics, and resulting external state.

Do not expose secrets to untrusted pull-request code, persist credentials in artifacts or caches, or make a failing required check appear successful.
