# Provider Compatibility

This matrix records the runtime assumptions verified by the harness. Run `python scripts/doctor.py` on each machine rather than assuming an installed version behaves the same.

| Provider | Personal instructions | Personal skills | Required behavior |
|---|---|---|---|
| Codex CLI | `~/.codex/AGENTS.md` | `~/.codex/skills/<name>/SKILL.md` | Codex loads global instructions before repository and nested instructions. Later scoped instructions may override earlier defaults. |
| Claude Code | `~/.claude/AGENTS.md` | `~/.claude/skills/<name>/SKILL.md` | Claude Code 2.1.277 or newer with `agents-md@builtin.options.instructionFiles` set to `claude-md-and-agents-md`. |

Claude's default `claude-md-or-agents-md` behavior yields to a repository `CLAUDE.md`. The harness selects `claude-md-and-agents-md` so the portable baseline remains active alongside repository-specific Claude instructions without creating another `CLAUDE.md`. Native `AGENTS.md` support was initially unavailable on Bedrock, Vertex, and Foundry; verify current provider documentation and the actual session before relying on it there.

The Agent Skills file format is portable, but discovery directories are runtime-specific. The installer therefore publishes validated copies to each runtime's supported personal skill directory.

Sources: [Codex instruction loading](https://developers.openai.com/api/docs/guides/latest-model), [Claude Code AGENTS.md implementation](https://github.com/anthropics/claude-code/blob/main/mods/agents-md/README.md), and the [Agent Skills specification](https://agentskills.io/specification).
