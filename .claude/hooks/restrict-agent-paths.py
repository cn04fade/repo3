"""PreToolUse hook that limits which folders the proof agents may access.

Usage (from an agent's frontmatter):
    python -I restrict-agent-paths.py <role>
where <role> is "generator", "reviewer" or "simplifier".

Claude Code passes the tool call as JSON on stdin. The script exits with
code 0 to allow the call, or with code 2 to block it; on a block, the
message on stderr is shown to the agent so it knows why.
"""

import json
import os
import re
import sys

# Folders (relative to the project root) each role may read from / write to.
RULES = {
    "generator": {
        "read": ["proof-exchange", "workflows", "resources"],
        "write": ["proof-exchange"],
        "forbidden_names": [],
    },
    "reviewer": {
        "read": ["proof-exchange"],
        "write": ["proof-exchange"],
        # The reviewer must judge only the written proof, not the
        # generator's reasoning.
        "forbidden_names": ["generator-report.md"],
    },
    "simplifier": {
        "read": ["proof-exchange"],
        "write": ["proof-exchange"],
        "forbidden_names": [],
        # The simplifier works from the problem and the proof only, and may
        # create only its own files, so the original proof stays untouched.
        "read_names": r"problem\.md|candidate\.md",
        "write_names": r"(simplified-proof|simplification-report)(-[2-9]|-[1-9][0-9]+)?\.md",
        "no_overwrite": True,
    },
}

WRITE_TOOLS = {"Write", "Edit", "NotebookEdit"}
FILE_TOOLS = WRITE_TOOLS | {"Read"}


def block(message):
    """Reject the tool call and tell the agent why."""
    print(message, file=sys.stderr)
    sys.exit(2)


def to_windows_path(path):
    """Turn a Git Bash style path like /c/Users/... into C:/Users/..."""
    if len(path) >= 3 and path[0] == "/" and path[2] == "/" and path[1].isalpha():
        return path[1] + ":" + path[2:]
    return path


def normalize(path, base):
    """Return an absolute, symlink-free, case-normalized version of path."""
    path = to_windows_path(path)
    if not os.path.isabs(path):
        path = os.path.join(base, path)
    return os.path.normcase(os.path.realpath(path))


def is_inside(path, folder):
    """True if path equals folder or lies somewhere below it."""
    try:
        return os.path.commonpath([path, folder]) == folder
    except ValueError:  # different drives
        return False


def target_paths(tool_name, tool_input):
    """Collect every path the tool call would touch."""
    if tool_name in ("Read", "Write", "Edit"):
        return [tool_input.get("file_path")]
    if tool_name == "NotebookEdit":
        return [tool_input.get("notebook_path")]
    if tool_name in ("Glob", "Grep"):
        pattern = tool_input.get("pattern", "")
        if tool_name == "Glob" and (os.path.isabs(to_windows_path(pattern)) or ".." in pattern):
            block("Glob patterns must be relative and must not contain '..'. "
                  "Pass the folder as 'path' instead.")
        if ".." in tool_input.get("glob", ""):
            block("Grep 'glob' filters must not contain '..'.")
        return [tool_input.get("path")]
    return []


def main():
    """Read the tool call from stdin and allow or block it."""
    role = sys.argv[1] if len(sys.argv) > 1 else ""
    if role not in RULES:
        block(f"restrict-agent-paths: unknown role '{role}'.")
    rules = RULES[role]

    data = json.load(sys.stdin)
    tool_name = data.get("tool_name", "")
    tool_input = data.get("tool_input", {}) or {}
    root = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or os.getcwd()
    root = os.path.realpath(to_windows_path(root))

    is_write = tool_name in WRITE_TOOLS
    allowed = rules["write"] if is_write else rules["read"]
    allowed_abs = [normalize(folder, root) for folder in allowed]
    allowed_text = ", ".join(folder + "/" for folder in allowed)

    for raw in target_paths(tool_name, tool_input):
        if not raw:
            block(f"{tool_name} needs an explicit path. Allowed folders: {allowed_text}")
        path = normalize(raw, root)
        if not any(is_inside(path, folder) for folder in allowed_abs):
            action = "write to" if is_write else "access"
            block(f"Blocked: the {role} agent may only {action} {allowed_text} "
                  f"(requested: {raw}).")
        if os.path.basename(path) in rules["forbidden_names"]:
            block(f"Blocked: the {role} agent may not read {os.path.basename(path)}.")
        name_pattern = rules.get("write_names" if is_write else "read_names")
        if name_pattern and tool_name in FILE_TOOLS and not re.fullmatch(name_pattern, os.path.basename(path)):
            action = "write" if is_write else "read"
            block(f"Blocked: the {role} agent may not {action} {os.path.basename(path)}.")
        if is_write and rules.get("no_overwrite") and os.path.exists(path):
            block(f"Blocked: {os.path.basename(path)} already exists. Use the next free number.")

    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as error:  # fail closed: an unexpected error must block, not allow
        block(f"restrict-agent-paths: could not check this tool call ({error}).")
