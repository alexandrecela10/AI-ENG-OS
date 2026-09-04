# Agent Design Patterns

Start with the simplest thing that could work. Most "agents" should be a single call with good retrieval; many of the rest should be a fixed workflow. Reach for an autonomous loop only when the number of steps genuinely can't be known in advance.

## The ladder

| Level | Shape | Use when | Eval |
|---|---|---|---|
| 0 | Single call | task fits in one prompt | task accuracy |
| 1 | Prompt chain | fixed sequence of transformations | per-step accuracy + end-to-end |
| 2 | Routing | classify, then dispatch to a specialised prompt | routing accuracy × downstream |
| 3 | Parallel / map-reduce | independent sub-tasks, or voting | agreement, end-to-end |
| 4 | Orchestrator–workers | dynamic decomposition, bounded fan-out | end-to-end task success, cost per success |
| 5 | Autonomous tool loop | open-ended tasks with verifiable progress | task success, steps to success, cost, safety |

## Components of a tool loop (see `scaffolds/agent-loop/`)

- **Tool registry**: typed schemas (`/tool-schema`), one clear purpose each, errors returned as data the model can act on.
- **Loop**: model → tool call(s) → results → model. Cap steps. Cap wall-clock. Cap tokens and dollars (budget guard).
- **State**: what the agent has seen and done, compacted when long. Decide what's in context vs retrievable.
- **Stop conditions**: explicit done signal, budget exhausted, repeated identical action, human requested.
- **Human gate**: any irreversible or externally visible action (send, delete, pay, deploy) requires approval. Named human, logged.
- **Tracing**: every step logged with inputs, outputs, tool args, latency, cost. Traces are how you debug and how you build evals.

## Reliability patterns

- **Verify, don't trust**: after the agent claims done, run a checker (tests, schema, second model) before accepting.
- **Reflection with a budget**: one critique-and-retry pass usually helps; unbounded reflection loops burn money.
- **Idempotent tools**: retries must be safe.
- **Fail closed**: on tool error or budget hit, stop and report, don't improvise.
- **Small tool surface**: fewer, well-described tools beat many overlapping ones. Measure tool-selection accuracy.
- **Context hygiene**: put tool results in clearly delimited blocks; summarise long results; never let retrieved content masquerade as instructions.

## Evaluating agents

- End-to-end task success is the metric that matters; step-level metrics explain it.
- Report steps-to-success, cost-per-success, p95 wall-clock, and rate of budget exhaustion.
- Build the eval set from traces: real tasks, graded by outcome checks where possible.
- Safety: rate of attempted gated actions, prompt-injection success rate via tool results.

## Anti-patterns

- Multi-agent for its own sake. Every extra agent is another prompt to version and another failure surface.
- Free-text tool arguments.
- No step cap ("it'll stop when it's done").
- Debugging from logs without traces.
