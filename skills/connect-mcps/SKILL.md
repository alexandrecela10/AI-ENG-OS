---
name: connect-mcps
description: Connect experiment-tracking, tracing, data and ops tools (Weights & Biases, Braintrust, Langfuse, Hugging Face, GitHub, Linear, Slack, Datadog) as MCP servers so skills can read live runs, traces and incidents instead of files.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/connect-mcps                          → list what's connected and what each skill would use it for
/connect-mcps connect to langfuse
/connect-mcps connect to wandb
```

**What you get:** the MCP config entry for the tool (written to the working repo's MCP config, never to `{ai-eng-os}`), an updated "Connected" line for the working repo's `CLAUDE.md` or `AGENTS.md`, and a note on which skills now read live data.

**Time:** 5–10 minutes per tool, plus getting an API key.

---

# /connect-mcps

Everything in the OS works without MCPs. They replace file lookups with live queries.

## Routing once connected

| Tool | Skills that use it | Replaces |
|---|---|---|
| Langfuse / Braintrust / W&B | `/eval-run-report`, `/trace-debug`, `/prompt-iterate`, `/weekly-review` | `outputs/experiments/*/results.jsonl`, `outputs/traces/` |
| Hugging Face | `/dataset-card`, `/literature-scan`, `/finetune-plan` | `context-library/datasets/` |
| GitHub | `/prompt-regression --setup-ci`, `/changelog`, `/decision-doc` | manual PR links |
| Linear | `/launch-readiness` conditions, `/incident-postmortem` actions | `outputs/tickets/` |
| Slack | `/status-update` delivery, incident timelines | copy-paste |
| Datadog | `/incident-postmortem` timeline, `/rollout-plan` alerts | manual exports |

## Steps

1. Ask which tool, and whether the API key is already in the project's secret store or env. Never paste keys into files.
2. Write the MCP server entry in the working repo's MCP config (the file the engineer's Devin/Claude setup reads); reference the key by env var name.
3. Test with one read call (list projects / list recent runs). Report what came back.
4. Update the "Connected" line in the working repo's rules file (offer, don't force).

## Rules

- Keys via env vars or the secret store only.
- Config goes in the working repo, not the plugin.
- If a tool has no MCP server yet, say so and fall back to files.
