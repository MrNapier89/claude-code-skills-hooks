---
name: explain-codebase
description: Use when the user is new to a codebase or asks how something works: produces a map of the architecture, entry points, data flow and where to make common changes.
---

# Explain a Codebase

1. Survey: top-level tree (2 levels), README, package/manifest files, entry points (main, index, app, cli), config files.
2. Trace one real request/command end to end through the code.
3. Output:
   - **What it is** (2 sentences)
   - **Map**: folder → responsibility (table)
   - **Flow**: numbered steps for the traced request with file:function references
   - **Key concepts/data models** (5-10)
   - **Where to change X**: for the 5 most likely tasks (add an endpoint, change a setting, add a test...)
   - **Gotchas**: surprising behaviour, tech debt, missing tests
Keep it under 2 pages. Link files as path:line.
