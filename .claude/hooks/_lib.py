"""Shared helpers for Claude Code hooks (stdin JSON in, decision out)."""
import json, sys

def read_input():
    try:
        return json.load(sys.stdin)
    except Exception:
        return {}

def deny(reason, event="PreToolUse"):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": event,
          "permissionDecision": "deny", "permissionDecisionReason": reason}}))
    sys.exit(0)

def ask(reason, event="PreToolUse"):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": event,
          "permissionDecision": "ask", "permissionDecisionReason": reason}}))
    sys.exit(0)

def block(reason):
    """Top-level block decision (PostToolUse / Stop / UserPromptSubmit): reason is shown to Claude."""
    print(json.dumps({"decision": "block", "reason": reason}))
    sys.exit(0)
