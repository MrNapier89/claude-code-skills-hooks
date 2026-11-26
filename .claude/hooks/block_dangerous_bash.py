#!/usr/bin/env python3
"""PreToolUse(Bash): deny destructive or irreversible shell commands; ask before risky ones."""
import re, sys, os; sys.path.insert(0, os.path.dirname(__file__))
from _lib import read_input, deny, ask
cmd = read_input().get("tool_input", {}).get("command", "")
DENY = [
    (r"\brm\s+(-[a-zA-Z]*r[a-zA-Z]*f|-[a-zA-Z]*f[a-zA-Z]*r)\s+(/|~|\$HOME|\*|\.)(\s|$)", "recursive force-delete of root/home/cwd"),
    (r"\bgit\s+push\b.*(--force\b|-f\b)(?!-with-lease)", "force push"),
    (r"\bgit\s+reset\s+--hard\b", "hard reset discards work"),
    (r"\bgit\s+clean\s+-[a-zA-Z]*f", "git clean deletes untracked files"),
    (r"\bmkfs(\.|\s)|\bdd\s+.*of=/dev/", "disk formatting/overwrite"),
    (r":\(\)\s*\{\s*:\|:&\s*\};:", "fork bomb"),
    (r"\b(chmod|chown)\s+-R\s+\S+\s+/(\s|$)", "recursive permission change on /"),
    (r"\bformat\s+[a-zA-Z]:", "Windows drive format"),
    (r"\bRemove-Item\b.*-Recurse.*-Force|\brd\s+/s\s+/q\s+[a-zA-Z]:\\\\?$", "recursive force delete (Windows)"),
]
ASK = [
    (r"\bgit\s+push\b", "pushing to a remote"),
    (r"\b(npm|pnpm|yarn)\s+publish\b|\btwine\s+upload\b|\bcargo\s+publish\b", "publishing a package"),
    (r"\bcurl\b.*\|\s*(ba)?sh\b|\bwget\b.*\|\s*(ba)?sh\b", "piping a download into a shell"),
    (r"\bDROP\s+(TABLE|DATABASE)\b|\bTRUNCATE\b", "destructive SQL"),
    (r"\bsudo\b", "running as root"),
]
for pat, why in DENY:
    if re.search(pat, cmd, re.I): deny(f"Blocked by hook: {why}. Ask the user to run it manually if truly intended.")
for pat, why in ASK:
    if re.search(pat, cmd, re.I): ask(f"Hook: this command involves {why}. Confirm?")
sys.exit(0)
