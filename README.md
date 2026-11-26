# Free Claude Code Skills & Hooks

Three skills and three hooks for [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) that I use on every project. Copy the `.claude/` folder into your repo and they work. No install, no dependencies beyond Python 3.

## What's inside

### Skills (`.claude/skills/`)

| Skill | What it does |
| --- | --- |
| `git-commit` | Groups your changes into clean Conventional Commits and refuses to stage `.env`, keys or build output. |
| `pr-description` | Writes a PR title and description from your branch: what, why, how to test, risks. |
| `explain-codebase` | Maps an unfamiliar repo: architecture, entry points, data flow, where to make common changes. |

### Hooks (`.claude/hooks/` + `.claude/settings.json`)

| Hook | Event | What it does |
| --- | --- | --- |
| `block_dangerous_bash.py` | PreToolUse (Bash) | Denies `rm -rf /`, force-push, `git reset --hard`, disk formatting. Asks before `git push`, `sudo`, `curl \| sh`, destructive SQL. |
| `protect_files.py` | PreToolUse (Edit/Write) | Claude can't touch `.env`, keys, lockfiles or `.git/`. Add your own globs in `.claude/protected.txt`. |
| `auto_format.py` | PostToolUse (Edit/Write) | Runs the right formatter (prettier, black/ruff, gofmt, rustfmt) after every edit, if it's installed. |

## Install

```bash
# from your project root
git clone https://github.com/MrNapier89/claude-code-skills-hooks /tmp/cc-free
cp -r /tmp/cc-free/.claude .
```

Already have a `.claude/settings.json`? Merge the `hooks` block instead of overwriting it.

Test that the safety hook works:

```bash
echo '{"tool_input":{"command":"rm -rf /"}}' | python .claude/hooks/block_dangerous_bash.py
# → permissionDecision: deny
```

## Want more?

These are taken from bigger, documented packs:

- **[Claude Code Hooks Examples](https://napier4.gumroad.com/l/claude-code-hooks-cookbook)**: 10 tested hooks (secret guard on prompts, run tests before "done", lint feedback, audit log, desktop notifications) plus a guide to how hooks work.
- **[Claude Code Skills Pack](https://napier4.gumroad.com/l/claude-code-dev-skills)**: 15 skills (code review, debug, write tests, security audit, refactor, SQL, release checklist…).
- **[Claude Code Agents Pack](https://napier4.gumroad.com/l/claude-code-subagent-team)**: 12 subagents (planner, reviewer, debugger, QA…).
- **[MCP Server Starter Kit](https://napier4.gumroad.com/l/mcp-server-starter-kit)**: Python + TypeScript MCP server templates.
- **[Free Claude Code Starter Kit](https://napier4.gumroad.com/l/claude-code-starter-kit)**: CLAUDE.md templates and 40 prompts, free.

Code `LAUNCH30` gives 30% off until December 3.

## License

MIT. Use it, fork it, ship it.
