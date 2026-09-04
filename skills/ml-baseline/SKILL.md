---
name: ml-baseline
description: Establish trivial and simple-model baselines (majority/mean/last-value, linear or tree) with CIs across seeds on the audited split, before any complex model. ML pack.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/ml-baseline outputs/ml/churn-framing.md
/ml-baseline --seeds 5 --models majority,logreg,gbm
```

**What you get:** `outputs/experiments/[date]-ml-baseline-[slug]/` with a manifest per baseline and `report.md`: metric (mean ± sd over seeds, bootstrap CI over test rows), per-slice, training cost, inference latency; the bar every later model must beat.

**Time:** 30–60 minutes.

---

# /ml-baseline

## Baselines

| Baseline | Purpose |
|---|---|
| trivial (majority class / mean / last value / seasonal naive) | floor; anything below this is broken |
| existing rule or current model | what you must beat in production |
| linear (logreg / ridge) with sane preprocessing | cheap, interpretable, often enough |
| gradient-boosted trees, default params | strong tabular baseline |

## Steps

1. Preconditions: split audit passed; metric chosen; test hash recorded.
2. Run each on val (and once on test for the report), 3+ seeds where stochastic.
3. Manifest per run (`change.type: training`, data hash, code sha, config, seed).
4. Report with CIs and slices. State the bar: "beat GBM 0.81 PR-AUC [0.78, 0.84] by more than the CI, or ship GBM."

## Rules

- Equal preprocessing across baselines.
- Test touched once for this report; log it.
- Never skip the trivial row.
