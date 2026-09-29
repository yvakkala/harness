---
name: bootstrap-durable-project
description: Create or productionize a durable software project when starting a new repository, establishing its engineering baseline, or promoting a quick experiment into maintained software. Do not use for ordinary feature work in an established project.
---

# Bootstrap a Durable Project

Establish the smallest project baseline that makes the intended software maintainable, verifiable, secure, and operable for its actual requirements.

## Workflow

1. Establish the product outcome, users or callers, supported environments, expected lifetime, data sensitivity, external exposure, and deployment target. Ask only for material facts the repository and prompt cannot answer.
2. Inspect any existing experiment or source before selecting a stack or structure. Preserve proven behavior and user work.
3. Propose one proportional plan when material architecture or platform choices remain. A direct stack or setup instruction needs no redundant plan.
4. Read [the durable baseline](references/durable-baseline.md) and select only the controls applicable to this product.
5. Build the thinnest end-to-end working path first, using red-green-refactor for meaningful durable behavior.
6. Add the selected project baseline around that working path. Avoid unused layers, example features, speculative abstractions, and placeholder infrastructure.
7. Verify the documented setup from a clean environment, run all required checks, inspect the initial repository state, and commit the complete baseline.

## Required outcome

- A new contributor or agent can install, run, test, build, and understand the project from its repository instructions.
- Configuration is validated, secrets stay outside source control, and test resources cannot affect non-test environments.
- CI enforces the checks the project claims to require.
- Production-facing behavior has only the security, logging, deployment, and recovery controls justified by its requirements.
- Promotion from a quick experiment replaces shortcuts that would make maintained use unsafe or unreliable.
