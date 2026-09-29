# CI Pipeline Review

## Trigger and trust boundary

- Distinguish trusted branch, fork, pull-request, schedule, manual, tag, and release events.
- Treat repository content from an untrusted contribution as attacker-controlled.
- Do not combine privileged secrets with checkout and execution of untrusted code.
- Review dynamic expressions, generated matrices, script interpolation, and event payload fields before placing them in shell commands.

## Dependencies and credentials

- Pin package-manager inputs with committed locks and install reproducibly.
- Pin non-platform actions, reusable workflows, containers, and build tools to reviewed immutable revisions when the ecosystem supports it.
- Declare token permissions explicitly and narrowly at workflow or job scope.
- Use short-lived identity federation instead of stored long-lived cloud credentials when available.

## Results and artifacts

- Run applicable formatting, linting, type, test, build, migration, and security checks without ignored failures.
- Retain concise failure evidence without secrets, unnecessary source bundles, or sensitive test data.
- Set artifact and cache retention deliberately and prevent untrusted writers from poisoning privileged consumers.
- Build release artifacts once and preserve source, dependency, workflow, and CI-result traceability.

## Efficiency and reliability

- Cancel superseded validation runs when safe.
- Parallelize independent jobs without creating ordering races.
- Use timeouts and concurrency controls for jobs and deployments.
- Keep a clear local reproduction command for every required check where practical.
