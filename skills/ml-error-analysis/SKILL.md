---
name: ml-error-analysis
description: Slice and read the errors of a model: where it fails (segments, ranges, time), confusion patterns, calibration, 50 hand-read cases, and the one change most likely to help. ML pack.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/ml-error-analysis outputs/experiments/2026-09-05-gbm-v3/predictions.csv
/ml-error-analysis --slices segment,tenure_bucket,month
```

**What you get:** `outputs/ml/error-analysis-[slug]-[date].md`: metric by slice with CIs, confusion / residual patterns, calibration curve summary, 50 hand-read cases grouped into failure clusters, hypotheses ranked, and the next single experiment.

**Time:** 45–60 minutes.

---

# /ml-error-analysis

## Steps

1. Metric per slice (given and discovered: by prediction confidence, input length, missingness, time). Flag slices below the trivial baseline.
2. Classification: confusion matrix; which classes are confused and why. Regression: residuals vs predicted, vs key features.
3. Calibration: reliability by bin; is the score usable as a probability?
4. Read 50 errors by hand (worst by loss, plus random). Cluster. Name each cluster.
5. Map clusters to causes: label noise, missing feature, leakage-in-reverse (feature unavailable at serve time), distribution shift, model capacity.
6. Rank hypotheses by (cluster size × plausibility ÷ effort). Propose one experiment → `/ml-ablation` or `/ml-training-plan`.
7. Offer rows for `failure-modes.md`.

## Rules

- Read the cases. Fifty.
- A slice collapse hidden by a good aggregate is a blocking finding for the model card.
