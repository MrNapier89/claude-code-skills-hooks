---
name: git-commit
description: Use when the user asks to commit: groups changes into logical commits with clear conventional-commit messages; never commits secrets or pushes without permission.
---

# Clean Commits

1. `git status` and `git diff` — understand every change.
2. Refuse to stage: `.env`, keys, tokens, credentials, large binaries, build output. Warn the user if they appear.
3. Group changes into logical commits (one purpose each). Stage per group with `git add -p` or specific paths.
4. Message format (Conventional Commits):
   ```
   <type>(<scope>): <imperative summary, ≤ 72 chars>

   <why this change, not what — wrap at 72>
   ```
   types: feat, fix, refactor, test, docs, chore, perf, build, ci
5. Never `git push`, `--force`, or rewrite history unless the user explicitly asks.
6. Show `git log --oneline -5` at the end.
