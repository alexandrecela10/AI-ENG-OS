# Metric Selection

Pick the metric from the decision, not from the library default.

| Decision the model drives | Metric | Why |
|---|---|---|
| binary action with a fixed threshold | precision/recall at that threshold, cost-weighted error | the business only sees the threshold |
| ranking / triage (top-k get attention) | precision@k, recall@k, nDCG | only the top matters |
| probability consumed downstream | log loss, Brier score, calibration curve | probabilities must mean what they say |
| imbalanced classes, positive class is what matters | PR-AUC, F-beta with beta chosen from cost ratio | ROC-AUC hides poor performance on rare positives |
| regression with asymmetric cost | quantile loss, cost-weighted MAE | over- and under-prediction cost differently |
| forecasting | MASE, sMAPE vs a seasonal-naive baseline | scale-free and beats-naive |
| multi-label | per-label F1 + macro/micro, coverage | aggregates hide label-level failures |

## Always report

- The trivial baseline on the same metric.
- CI (bootstrap over test rows; over seeds for the model).
- Per-slice values (segments, time periods).
- Calibration if any threshold will move after deployment.
- Cost per correct decision when models differ in inference cost.

## Traps

Accuracy on imbalanced data · ROC-AUC when positives are rare · aggregate metrics hiding a slice collapse · optimising a proxy metric with no link to the decision · comparing models tuned with unequal budgets.
