---
name: agent-design
description: Design a tool-using agent at the lowest viable level of autonomy, with typed tools, caps, tracing, stop conditions and a human gate. Copies and adapts {ai-eng-os}/scaffolds/agent-loop when the design calls for a loop.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/agent-design "agent that triages incoming tickets and drafts replies"
/agent-design --from outputs/design-docs/triage-design-v1.md --scaffold     → also copy the loop scaffold
/agent-design --review                                                       → run infra-reviewer and red-teamer on the design
```

**What you get:** `outputs/design-docs/[slug]-agent-design.md` (ladder level with justification, tool list with schemas, loop caps, state plan, stop conditions, gate list, tracing fields, eval plan), and with `--scaffold`, `outputs/scaffolds/agent-loop/` adapted with the tools stubbed.

**Time:** 1 hour.

---

# /agent-design

Most agents should be workflows. This skill makes you earn each step up the ladder.

## Context routing

`{ai-eng-os}/frameworks/agent-design-patterns.md` (ladder, components, reliability), `tool-schema-guidelines.md`, `safety-checklist.md` § agent-specific, `cost-latency-budgeting.md`. Project: brief (budgets), failure modes, existing tools/APIs in the repo.

## Steps

1. **Ladder check.** For each level 0→5, ask "would this work?" Stop at the first yes. Write why the lower levels don't.
2. **Tools.** List each with: purpose, read-only or side-effecting, inputs, outputs, error shape. Draft schemas (`/tool-schema` for the full treatment). Fewer is better; note overlaps.
3. **Loop.** Caps: steps, tokens, dollars, wall-clock. Stop conditions. Repeat detection. Fail-closed behavior.
4. **State.** What stays in context, what's summarised, what's retrieved.
5. **Human gate.** Every irreversible action listed with who approves and how it's logged.
6. **Tracing.** Fields per step: model in/out, tool name/args/result, tokens, cost, latency, version ids.
7. **Eval plan.** End-to-end task success from traces; steps-to-success; cost-per-success; budget-exhaustion rate; injection-via-tool-result success rate. → `/eval-spec`.
8. **Scaffold** (`--scaffold`): copy `agent-loop/`, stub the tools in `tools.py`, set caps in `Caps`, note where `call_model()` needs wiring.

## Review

`--review` runs `infra-reviewer.md` and `red-teamer.md`. Findings at the top of the doc.

## Rules

- No free-text tool arguments.
- No uncapped loop, ever.
- Tool results and retrieved content are data, delimited as such in the prompt.
- Side-effecting tools default to gated.
