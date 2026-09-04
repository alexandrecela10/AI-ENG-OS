# Test Selection Guide

Start from the data type and the design, not from the test you remember. Report the CI on the effect, whatever the test.

## By outcome type and design

| Outcome | Two groups, independent | Two conditions, paired (same items) | >2 groups | Relationship |
|---|---|---|---|---|
| **binary** (pass/fail, converted) | two-proportion z / chi-square; CI: Newcombe or bootstrap | McNemar; CI on paired difference via bootstrap | chi-square + pairwise with correction | logistic regression |
| **continuous, roughly symmetric** | Welch t; CI on mean difference | paired t; CI on mean paired difference | ANOVA (Welch) → pairwise with correction | linear regression |
| **continuous, skewed / heavy tails** (latency, cost) | Mann-Whitney or bootstrap CI on difference of means/medians; consider log transform | Wilcoxon signed-rank or bootstrap on paired diffs | Kruskal-Wallis | quantile regression |
| **ordinal** (1–5 rubric) | Mann-Whitney; report distribution, not just mean | Wilcoxon signed-rank | Kruskal-Wallis | ordinal regression |
| **counts / rates** | Poisson / negative-binomial regression | paired: difference in rates with bootstrap | regression | regression |
| **time-to-event** | log-rank; Cox | — | log-rank | Cox |

## Eval-specific defaults

- **Two prompt/model versions on the same golden set** → paired. Per-item difference, bootstrap CI on the mean difference (`stats.paired_delta_ci` in the harness). Never treat as independent samples; you'd overstate the uncertainty.
- **Pass rate of one system** → Wilson interval.
- **LLM-judge 1–5 scores** → treat as ordinal; report the distribution and share ≥ 4; Wilcoxon for paired comparison.
- **Latency** → report p50/p95 with bootstrap CIs; compare on log scale or with quantile bootstrap.
- **Non-deterministic runs** → repeats are the unit; report between-run sd; a single run is one sample.
- **A/B on users** → unit is the user, not the request; cluster or aggregate per user first.

## Assumptions to check before trusting a parametric test

Independence of observations (clustering by user/session/document breaks it) · roughly normal sampling distribution of the mean (large n helps; heavy tails hurt) · similar variances (use Welch by default) · for paired: pairs are genuinely matched.

When in doubt, bootstrap. It's rarely wrong and always reportable.
