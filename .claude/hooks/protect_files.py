#!/usr/bin/env python3
"""PreToolUse(Edit|Write|MultiEdit): never let Claude modify secrets, lockfiles, git internals or protected folders."""
import fnmatch, os, sys; sys.path.insert(0, os.path.dirname(__file__))
from _lib import read_input, deny
data = read_input(); ti = data.get("tool_input", {})
path = (ti.get("file_path") or ti.get("path") or "").replace("\\", "/")
PROTECTED = [".env", ".env.*", "*.pem", "*.key", "id_rsa*", "*credentials*.json", "*secret*",
             "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "poetry.lock", "Cargo.lock",
             ".git/*", "*/.git/*", "input/*", "*/input/*"]
# Add your own patterns in .claude/protected.txt (one glob per line)
extra = os.path.join(os.environ.get("CLAUDE_PROJECT_DIR", "."), ".claude", "protected.txt")
if os.path.exists(extra):
    PROTECTED += [l.strip() for l in open(extra, encoding="utf-8") if l.strip() and not l.startswith("#")]
name = os.path.basename(path)
for pat in PROTECTED:
    if fnmatch.fnmatch(path, pat) or fnmatch.fnmatch(name, pat):
        deny(f"'{path}' is protected (matches '{pat}'). Edit it manually if needed.")
sys.exit(0)
