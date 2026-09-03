# Leakage Checklist

Leakage is the most common reason an ML result doesn't survive production. Run before the first training run and again before the model card.

## Split-level

- [ ] Unit of split matches deployment: time (train on past, test on future), user/entity (no user in both), group (sessions, documents, patients).
- [ ] No exact or near-duplicate rows across splits (hash + near-dup).
- [ ] Test set frozen with a hash; touched once per shippable candidate.
- [ ] Validation used for tuning is separate from test.
- [ ] Overlap with any LLM golden set in `context-library/evals/` is zero.

## Feature-level

- [ ] No feature computed using data from after the prediction time (target leakage, future aggregates, "days until churn").
- [ ] No feature that is a proxy for the label (e.g. "refund issued" when predicting complaints).
- [ ] Aggregates (means, counts, encodings) fitted on train only, then applied to val/test.
- [ ] Scaling, imputation, target encoding, feature selection all inside the pipeline fitted on train.
- [ ] Row ids, timestamps or ordering that correlate with the label are excluded or justified.

## Process-level

- [ ] Hyperparameter search used validation only.
- [ ] Early stopping used validation only.
- [ ] Any "quick look" at test results is logged as a test-set touch.
- [ ] Data used for training the model isn't in the eval set for a downstream LLM system that consumes it.

## Sanity checks that catch leakage

- Suspiciously high performance vs the trivial baseline (> 20 pts on a hard task).
- A single feature with dominant importance; check its provenance.
- Shuffle the labels: the model should drop to chance.
- Train on future, test on past: if it still works, features may carry time.
