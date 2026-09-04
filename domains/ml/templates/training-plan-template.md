# Training Plan: [model / task] v[ ]

**Owner:** [ ] · **Date:** [ ] · **Framing doc:** [link] · **Data card:** [link] · **Split audit:** [link]

## Target and metric

Prediction target: [ ]. Decision it drives: [ ]. Primary metric: [ ] (why: see `metric-selection.md`). Guardrail metrics: [ ]. Bar to beat: [trivial baseline value], [simple model value] with CIs.

## Data

Train / val / test sizes; split unit; hash of test; leakage checklist date.

## Candidates

| Model | Why | Tuning budget (trials / GPU-h) | Seeds |
|---|---|---|---|
| linear / tree baseline | | | 3 |
| [candidate A] | | same | 3 |

## Training config

Features and preprocessing (inside pipeline); loss; optimiser; early stopping on val; checkpointing; compute budget; expected runtime and cost.

## Experiment tracking

Each run → `outputs/experiments/<id>/manifest.json` (change type `training`) with data hash, code sha, config, seed, metrics with CI, cost.

## Success / stop criteria

Ship if [metric] >= [ ] and guardrails hold. Stop if best candidate is within CI of the simple baseline after [budget].

## Risks

Leakage, drift between train window and deployment, training/serving skew, class imbalance, label noise. Mitigation per risk.
