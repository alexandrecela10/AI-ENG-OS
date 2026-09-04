# agent-loop

A tool-using loop with the guardrails that are always missing from the first version: typed tool registry, step/token/dollar/wall-clock caps, tracing on every step, and a human gate for irreversible actions.

```
agent-loop/
├── tools.py     # @tool decorator -> registry with JSON schemas; read_only flag
├── loop.py      # run(task) -> Result; caps; fail-closed; trace hooks
└── gate.py      # human approval for side-effecting tools (CLI stub; replace with Slack/UI)
```

Replace `call_model()` in `loop.py` with the project's client (must support tool calling). Keep the caps.

Eval it with `/eval-spec` on end-to-end task success, steps-to-success, cost-per-success and budget-exhaustion rate. Build the eval set from traces.
