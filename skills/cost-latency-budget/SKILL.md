---
name: cost-latency-budget
description: Set or check the cost and latency budget for a system, project spend at expected and 10x volume, rank the levers (routing, caching, prompt trimming, output caps, batching), and propose the next experiment.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/cost-latency-budget                                       → set budgets from the brief and current runs
/cost-latency-budget --check outputs/experiments/2026-09-03-v5/   → is this run within budget at volume?
/cost-latency-budget --levers                              → ranked cost/latency experiments
```

**What you get:** `outputs/reports/cost-latency-[date].md`: budget table (target vs current vs 10× projection), where tokens and time go, ranked levers with expected effect and risk to accuracy, and one experiment ready for `/eval-spec`.

**Time:** 20 minutes.

---

# /cost-latency-budget

Use `{ai-eng-os}/frameworks/cost-latency-budgeting.md`.

## Steps

1. **Budget.** From the brief: $/1k, p50/p95, token caps. If missing, derive from unit economics with the user and write them into the brief (offer, don't force).
2. **Current.** From the latest manifest: cost/1k, p50, p95, input/output tokens per request, cache hit share if known.
3. **Projection.** Expected volume and 10×. Flag where the ceiling breaks.
4. **Breakdown.** Input vs output tokens; system prompt share; retrieved context share; agent steps.
5. **Levers.** Rank by expected saving ÷ accuracy risk. Each lever is a one-variable experiment with the gated metrics as guardrails.
6. **Decision metric.** Report cost per correct answer alongside accuracy for any model comparison.

## Rules

- Cost and latency changes go through the same eval loop as accuracy changes.
- Caps and alerts are part of the budget, not an afterthought.
