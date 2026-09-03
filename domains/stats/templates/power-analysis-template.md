# Power Analysis: [eval / experiment]

**Owner:** [ ] · **Date:** [ ] · **For:** [eval spec / A/B / causal plan link]

## Inputs

| Input | Value | Source |
|---|---|---|
| Outcome type | binary / continuous / ordinal / rate | |
| Design | paired items / independent groups / clustered | |
| Baseline value | [e.g. pass rate 0.81] | baseline run [id] |
| Baseline variability | [sd, or per-item disagreement rate for paired binary] | |
| Minimum effect worth detecting | [e.g. +3 pts] | decision rule |
| α (two-sided) | 0.05 | |
| Power (1−β) | 0.80 / 0.90 | |
| Number of primary comparisons | [k] → corrected α = [ ] | |
| Clustering | [ICC, cluster size] | |

## Result

Required n = [ ] per arm (or items, for paired). With available n = [ ], detectable effect = [ ]; power for the minimum effect = [ ].

## Sensitivity

n under optimistic / pessimistic variability. Plot or small table.

## Decision

Run as planned / collect more items / accept lower power and label exploratory / change the design (pair items, reduce metrics).

## Method

Formula or simulation used; code link. Simulation preferred for paired binary, ordinal and clustered designs.
