---
name: rollout-plan
description: Write the rollout plan for a change: strategy (shadow, canary, ramp, A/B), stage table with promotion and rollback criteria, monitoring during rollout, tested rollback, comms.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/rollout-plan --release v5
/rollout-plan --strategy ab --duration 14d        → when the question is user impact, not just safety
```

**What you get:** `outputs/reports/rollout-[system]-v[n].md` from `{ai-eng-os}/templates/rollout-plan-template.md`.

**Time:** 20–30 minutes.

---

# /rollout-plan

Use `{ai-eng-os}/frameworks/rollout-strategies.md`.

## Steps

1. **Pick the strategy** by the question: "does it break?" → shadow + canary + ramp; "did users benefit?" → A/B (hand the analysis design to `/causal-question` and `/stats-power`).
2. **Stage table**: traffic, duration (cover the traffic cycle), promote-if criteria (gated metrics within CI, p95, error rate, cost), roll-back-if triggers, owner per stage.
3. **Monitoring**: dashboards, alerts with thresholds, human review sampling (n/hour, who).
4. **Rollback**: the action, time to execute, data implications, last tested date. If untested, schedule the test as a condition.
5. **Comms**: before/during/after; `/changelog` after.

## Rules

- Criteria written before the rollout starts, not adjusted during.
- Provider snapshot bumps get their own rollout.
- `ops-reviewer.md` reviews on request.
