---
name: ml-monitoring-plan
description: Write the production monitoring plan for a model: input and prediction drift, delayed-label performance, calibration, slices, data quality, retraining triggers and rollback. ML pack.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/ml-monitoring-plan --model churn-gbm-v3
/ml-monitoring-plan --label-latency 30d
```

**What you get:** `outputs/ml/monitoring-plan-[model].md` from `{ai-eng-os}/domains/ml/templates/monitoring-plan-template.md`, plus a proposed row set for the launch-readiness doc.

**Time:** 30 minutes.

---

# /ml-monitoring-plan

## Steps

1. Signals: input drift (PSI/KL on key features), prediction drift, performance when labels arrive, calibration, slice performance, data quality, latency/cost.
2. Thresholds from the training-window variance and the business floor; windows from label latency.
3. Label latency and the proxy metric used meanwhile.
4. Retraining: trigger, window, validation against the frozen test (hash), promotion and rollback path.
5. Human review sample per week; where findings go.
6. Owners for each alert.

## Rules

- No monitoring plan, no launch readiness.
- Every alert names a person and an action.
