# Assumption Checks

What to run and report for each strategy. A check that isn't reported is assumed failed by the reviewer.

## All designs

- Pre-registration: estimand, primary outcome, sample size, analysis, stopping rule written before looking (`templates/causal-analysis-plan-template.md`).
- Covariate balance table (standardised mean differences; < 0.1 is the usual bar).
- Effect over time plot.
- CI on the effect; Bayesian posterior if a decision needs a probability.
- Heterogeneity: pre-specified subgroups only, or clearly exploratory.

## RCT / A/B

- SRM chi-square on assignment counts.
- Balance on pre-period outcome and key covariates.
- Interference risk statement (units share a market, a team, a feed?).
- Guardrail metrics.

## DiD

- Event-study plot with pre-period coefficients near zero.
- Placebo: fake treatment date in the pre-period.
- Staggered adoption: use an estimator that handles heterogeneous timing; report which.
- Cluster standard errors at the assignment level.

## IV

- First-stage F-statistic (report; weak if < 10).
- Reduced form.
- Exclusion restriction: argued in prose with the DAG; name the most plausible violation.
- Monotonicity argument.
- Compliers described.

## RDD

- Density test at the cutoff.
- Covariate smoothness across the cutoff.
- Bandwidth sensitivity plot.
- Placebo cutoffs.
- Local linear vs polynomial comparison (prefer local linear).

## Synthetic control

- Pre-period RMSPE and fit plot.
- In-space placebos (every donor as if treated) → permutation p-value.
- In-time placebo.
- Leave-one-donor-out.

## Matching / weighting / adjustment

- Overlap (propensity distributions).
- Balance after adjustment.
- Sensitivity to unmeasured confounding (Rosenbaum bounds, E-value, or coefficient-stability).
- Specification: doubly robust or at least two specifications agreeing.

## Reporting

For each check: what, result, pass/fail/caveat, plot link. Put them in the writeup's "Assumptions and checks" table.
