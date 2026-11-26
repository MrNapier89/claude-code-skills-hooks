---
name: pr-description
description: Use to write a pull request title and description from the current branch: summary, why, how to test, risks.
---

# PR Description

1. Gather: `git log main..HEAD --oneline`, `git diff main...HEAD --stat`, and the diff of the key files.
2. Write:
```
## What
<2-4 bullets, user-visible effect first>

## Why
<the problem or ticket, 1-3 sentences>

## How to test
1. <exact commands / clicks>
2. <expected result>

## Risks & rollout
<migrations, config changes, breaking changes, feature flags — or "None">
```
3. Title: imperative, ≤ 70 characters, no ticket noise unless the team uses it.
