from typing import Any


def approve(tool_name: str, args: dict[str, Any], trace_id: str) -> bool:
    """Human gate for side-effecting tools. Replace with Slack/UI approval. Log every decision."""
    print(f"[gate] {trace_id} wants to run {tool_name}({args}). Approve? [y/N] ", end="", flush=True)
    return input().strip().lower() == "y"
