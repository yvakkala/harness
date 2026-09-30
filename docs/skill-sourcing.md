# Skill Sourcing Decisions

**Reviewed:** 2026-09-30  
**Policy:** Prefer a small catalog of narrow, tested skills. Reuse licensed skills unchanged when they fit, adapt valuable techniques when local requirements differ, write personal policy skills locally, and reject overlapping framework ceremony.

## Pinned upstream revisions

| Source | Revision reviewed | License note |
|---|---|---|
| [OpenAI Plugins](https://github.com/openai/plugins) | `5fd93af4cd0c623e020d0cc7e9ce178b4ac1f70f` | License varies by plugin or skill; absence of a reusable license means reference only. |
| [Anthropic Skills](https://github.com/anthropics/skills) | `8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4` | Many skills are Apache-2.0; document skills are source-available. Check each skill's `LICENSE.txt`. |
| [Superpowers](https://github.com/obra/superpowers) | `8ca22dba9a94f28898bbce59f2537ff4d87c747d` | MIT. Adapted material must retain attribution and license. |

The deprecated `openai/skills` catalog is not an upstream dependency. Current OpenAI examples come from `openai/plugins`.

## Decisions

| Candidate | Source | Decision | Reason |
|---|---|---|---|
| `systematic-debugging` | Superpowers | Adapt | Evidence-first diagnosis is valuable. The local version removes absolute ceremony, cross-skill dependencies, the three-attempt rule, and unsafe diagnostic examples; it uses the owner's two-attempt policy. |
| `verification-before-completion` | Superpowers | Absorb into `AGENTS.md` | Verification is universal and should not depend on skill triggering. The local core uses evidence without the original accusatory language or repeated ceremony. |
| `test-driven-development` | Superpowers | Absorb into `AGENTS.md` | TDD is a durable default with locally approved exclusions. The upstream skill is broader and more absolute than the approved policy. |
| `using-git-worktrees` | Superpowers | Defer | Worktrees are useful for some parallel or isolated work, but they are not a universal workflow and delegation is disabled by default. |
| `using-superpowers` | Superpowers | Reject | Mandatory skill invocation before every response creates context cost and unnecessary ceremony. |
| `brainstorming`, `writing-plans`, `executing-plans` | Superpowers | Reject as global workflow | They conflict with one proportional plan approval and direct execution for precise changes. Individual techniques may be reconsidered for a demonstrated gap. |
| Subagent and mandatory review skills | Superpowers | Reject as default | They conflict with `delegation: false` and the prohibition on forced agent-per-task workflows. |
| `react-best-practices` and frontend testing skills | OpenAI Plugins | Project opt-in | Useful for applicable web stacks, but too technology-specific for the personal global catalog. Review the plugin license and current framework version when adopted. |
| Expo skills | OpenAI Plugins | Project opt-in | Valuable for React Native or Expo projects. Install only in those repositories and preserve their upstream update path. |
| Codex security skills | OpenAI Plugins | Project or task opt-in | Useful for explicit security audits and finding remediation. Ordinary security-sensitive implementation uses the smaller local routing skill. |
| `webapp-testing` | Anthropic Skills | Project opt-in | A useful browser-testing reference when its tool assumptions match the environment. It is not needed for every project. |
| `skill-creator` | OpenAI and Anthropic | Development reference | Use the installed creator when maintaining this catalog; do not add another always-visible duplicate. |
| Document creation skills | Anthropic Skills | Install unchanged when needed | They are specialized capabilities with individual licenses. Do not fork source-available skills without compatible terms. |

## Local skills

The following skills encode personal requirements or bridge a demonstrated gap:

- `bootstrap-durable-project`
- `logging-observability`
- `database-migration`
- `api-contract`
- `security-sensitive-change`
- `user-interface-delivery`
- `release-deploy`
- `systematic-debugging` (adapted from Superpowers)
- `infrastructure-change`
- `ci-pipeline`

## Admission checklist

Before adding or updating an external skill:

1. Name the repeated task or demonstrated failure it addresses.
2. Confirm the skill is narrower than the always-active core and does not duplicate another skill.
3. Review every instruction, script, hook, dependency, network action, and requested permission.
4. Verify the license permits the intended use and modification.
5. Pin the reviewed upstream revision and record local differences.
6. Remove provider-specific assumptions unless they are essential to the skill.
7. Test realistic triggering, non-triggering, and failure cases in isolation.
8. Install only after it improves outcomes without disproportionate context or ceremony.
9. Review upstream changes explicitly; never auto-update executable skill content.
