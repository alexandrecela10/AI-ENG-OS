"""Tool loop with caps, tracing and a human gate. Replace call_model() with the project's client."""
import json
import time
import uuid
from dataclasses import dataclass, field
from typing import Any

import tools
from gate import approve


@dataclass
class Caps:
    max_steps: int = 15
    max_tokens: int = 60_000
    max_usd: float = 1.00
    max_seconds: float = 120.0


@dataclass
class Result:
    status: str  # "done" | "budget_exhausted" | "gate_denied" | "error"
    answer: str | None
    steps: int
    tokens: int
    usd: float
    seconds: float
    trace_id: str
    events: list[dict[str, Any]] = field(default_factory=list)


PRICE_PER_1K = {"input": 0.003, "output": 0.015}


def call_model(system: str, messages: list[dict], tool_schemas: list[dict]) -> dict:
    """Return {"text": str | None, "tool_calls": [{"id","name","args"}], "usage": {"input_tokens","output_tokens"}}. REPLACE ME."""
    raise NotImplementedError


def trace(events: list[dict], **ev: Any) -> None:
    ev["t"] = time.time()
    events.append(ev)  # swap for Langfuse/Braintrust/W&B client


def run(task: str, system: str, caps: Caps = Caps()) -> Result:
    trace_id = uuid.uuid4().hex[:12]
    events: list[dict[str, Any]] = []
    messages: list[dict[str, Any]] = [{"role": "user", "content": task}]
    tokens, usd, steps, t0 = 0, 0.0, 0, time.perf_counter()
    last_call_sig = None

    while True:
        elapsed = time.perf_counter() - t0
        if steps >= caps.max_steps or tokens >= caps.max_tokens or usd >= caps.max_usd or elapsed >= caps.max_seconds:
            trace(events, kind="budget_exhausted", steps=steps, tokens=tokens, usd=usd)
            return Result("budget_exhausted", None, steps, tokens, usd, elapsed, trace_id, events)

        resp = call_model(system, messages, tools.schemas())
        steps += 1
        u = resp["usage"]
        tokens += u["input_tokens"] + u["output_tokens"]
        usd += u["input_tokens"] / 1000 * PRICE_PER_1K["input"] + u["output_tokens"] / 1000 * PRICE_PER_1K["output"]
        trace(events, kind="model", step=steps, usage=u, tool_calls=[c["name"] for c in resp["tool_calls"]])

        if not resp["tool_calls"]:
            return Result("done", resp["text"], steps, tokens, usd, time.perf_counter() - t0, trace_id, events)

        messages.append({"role": "assistant", "content": resp["text"], "tool_calls": resp["tool_calls"]})
        sig = json.dumps(resp["tool_calls"], sort_keys=True)
        if sig == last_call_sig:
            trace(events, kind="repeat_detected")
            messages.append({"role": "user", "content": "You repeated the same tool call. Change approach or finish."})
        last_call_sig = sig

        for c in resp["tool_calls"]:
            t = tools.REGISTRY.get(c["name"])
            if t and not t.read_only and not approve(c["name"], c["args"], trace_id):
                trace(events, kind="gate_denied", tool=c["name"])
                return Result("gate_denied", None, steps, tokens, usd, time.perf_counter() - t0, trace_id, events)
            out = tools.call(c["name"], c["args"])
            trace(events, kind="tool", tool=c["name"], args=c["args"], ok="error" not in (out if isinstance(out, dict) else {}))
            messages.append({"role": "tool", "tool_call_id": c["id"], "content": json.dumps(out, ensure_ascii=False)[:8000]})
