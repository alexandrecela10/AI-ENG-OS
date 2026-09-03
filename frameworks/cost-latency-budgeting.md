# Cost and Latency Budgeting

Accuracy without cost and latency is not a result. Set the budget before building; report against it in every run.

## Set the budget

- **Cost**: $ per 1k requests at expected volume, and the hard ceiling. Derive from unit economics or the team's compute budget. Write it in `project-brief.md`.
- **Latency**: p50 and p95 targets from the user experience (chat: p95 < 3–5 s to first token; batch: throughput matters, not latency).
- **Token budget per request**: input and output caps that make the cost budget hold.

## Where the money goes

| Lever | Typical effect | Cost to try |
|---|---|---|
| Smaller / cheaper model for easy cases (router) | 30–70% cost cut | medium; needs routing eval |
| Prompt caching of the stable prefix | 50–90% off input cost on cached share | low |
| Shorter system prompt, fewer few-shots | linear in tokens | low; measure accuracy |
| Truncate / summarise retrieved context | linear | low |
| Cap output tokens; ask for terse format | linear | low |
| Batch API for offline work | ~50% | low |
| Fewer agent steps (better tools, verify early) | large for agents | medium |
| Fine-tune a small model on the big model's outputs | large, if task is narrow | high |

## Where the time goes

- Time to first token ≈ input processing + queue. Long prompts hurt. Streaming hides output latency.
- Output tokens dominate total latency; cap them.
- Sequential tool calls add up; parallelise independent calls.
- Retrieval and reranking: measure; usually small next to generation.
- Tail latency (p95/p99) comes from long outputs, retries and provider variance. Set timeouts and fallbacks.

## Reporting

Every manifest and results table carries `cost_usd_per_1k`, `latency_ms.p50`, `latency_ms.p95`. Prefer **cost per correct answer** as the decision metric when comparing models.

## Guardrails in production

- Per-request token and dollar caps in the scaffold (budget guard).
- Alerts on daily spend, p95, and error rate. Thresholds in the rollout plan.
- Kill switch that falls back to the previous version or a cheap deterministic path.
