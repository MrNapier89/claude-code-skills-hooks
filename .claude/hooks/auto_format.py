#!/usr/bin/env python3
"""PostToolUse(Edit|Write|MultiEdit): format the edited file with the right formatter if it is installed."""
import os, shutil, subprocess, sys; sys.path.insert(0, os.path.dirname(__file__))
from _lib import read_input
ti = read_input().get("tool_input", {}); path = ti.get("file_path") or ""
if not path or not os.path.exists(path): sys.exit(0)
ext = os.path.splitext(path)[1].lower()
FORMATTERS = {
    (".py",): [["ruff", "format", path], ["black", "-q", path]],
    (".js", ".jsx", ".ts", ".tsx", ".json", ".css", ".scss", ".md", ".html", ".yaml", ".yml"): [["npx", "--no-install", "prettier", "--write", path]],
    (".go",): [["gofmt", "-w", path]],
    (".rs",): [["rustfmt", path]],
}
for exts, cmds in FORMATTERS.items():
    if ext in exts:
        for c in cmds:
            if shutil.which(c[0]):
                subprocess.run(c, capture_output=True, timeout=60); break
        break
sys.exit(0)
