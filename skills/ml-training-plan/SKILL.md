---
name: ml-training-plan
description: Write the training plan for a model candidate: data, candidates with equal tuning budgets, config, tracking, success and stop criteria, risks. ML pack.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/ml-training-plan outputs/ml/churn-framing.md --baseline outputs/experiments/2026-09-03-ml-baseline-churn/
/ml-training-plan --candidates gbm-tuned,mlp,transformer-tabular
```

**What you get:** `outputs/ml/training-plan-[slug]-v1.md` from `{ai-eng-os}/domains/ml/templates/training-plan-template.md`.

**Time:** 30 minutes.

---

# /ml-training-plan

## Steps

1. Pull target, metric, bar (baseline report), data card, split audit.
2. Candidates: each with a reason, an equal tuning budget, 3+ seeds.
3. Config: preprocessing inside the pipeline; loss aligned with the metric; early stopping on val; checkpoints; compute and cost estimate.
4. Tracking: manifest per run; what's logged.
5. Success/stop criteria in numbers; the stop criterion protects the budget.
6. Risks from `{ai-eng-os}/domains/ml/frameworks/leakage-checklist.md` and drift; mitigation per risk.
7. Review with `ml-reviewer.md` on request.

## Rules

- Unequal tuning budgets make comparisons meaningless; say the budget.
- The stop criterion is not optional.
