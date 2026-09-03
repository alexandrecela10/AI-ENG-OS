# ML Lifecycle

Same loop as the spine, with ML-specific gates.

```
frame → split (audit) → trivial baseline → simple model → eval → error analysis → one change → ablate → ... → monitoring plan → deploy gate
```

## Gates

| Gate | Must be true before moving on |
|---|---|
| Frame | prediction target defined, decision it drives named, metric chosen (`metric-selection.md`), cost of errors stated |
| Split | unit of split matches deployment (time / user / group); leakage checklist run; test set touched once |
| Baseline | majority/mean/last-value and a linear or tree baseline reported with CIs |
| Model | one change vs previous best; equal tuning budget across compared models; seeds reported |
| Error analysis | failures sliced; 50 read by hand; next change justified by what was seen |
| Ablation | each component's contribution isolated in a table |
| Ship | calibration checked if thresholds move; training/serving skew checked; monitoring plan written; model card |

## Rules of thumb

- Time-based split if the model will see the future. Always.
- If the fancy model beats the linear one by less than the CI, ship the linear one.
- Never tune on the test set. Never look at the test set more than once per candidate you'd ship.
- Report variance across seeds; a single run is an anecdote.
- Class imbalance: choose the metric first (PR-AUC, cost-weighted), then the technique.
- Feature importance is not causation. Hand causal questions to the causal pack.
