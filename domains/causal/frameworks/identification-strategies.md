# Identification Strategies

Pick the strategy from the data you have and the assumption you can defend, not from what's fashionable. State the key assumption in one plain sentence in every writeup.

| Strategy | When you have | Key assumption (plain) | Estimand | Checks |
|---|---|---|---|---|
| **RCT / A/B** | control over assignment | assignment is random | ATE | balance on pre-treatment covariates; SRM (sample-ratio mismatch); no interference |
| **Difference-in-differences** | treated and untreated groups, before and after | without treatment, both groups would have moved in parallel | ATT | pre-period parallel trends; event-study plot; placebo timing; staggered-adoption-aware estimator |
| **Instrumental variables** | a variable that shifts treatment but affects the outcome only through it | the instrument is as-good-as-random and has no other path to the outcome | LATE (for compliers) | first-stage F > 10 (weak instrument); exclusion argued, not tested; monotonicity |
| **Regression discontinuity** | treatment assigned by a threshold on a continuous score | units just above and below the cutoff are alike | local effect at the cutoff | density test at cutoff (McCrary); covariate smoothness; bandwidth sensitivity; placebo cutoffs |
| **Synthetic control** | one or few treated units, many untreated, long pre-period | a weighted combination of donors reproduces the treated pre-trend | effect for the treated unit | pre-period fit; in-time and in-space placebos; leave-one-donor-out |
| **Matching / weighting (PSM, IPW, DR)** | rich pre-treatment covariates | no unmeasured confounding given the covariates (conditional ignorability) | ATE / ATT | balance after adjustment; overlap; sensitivity to unmeasured confounding |
| **Regression adjustment** | same as above | same, plus correct functional form | ATE | same, plus specification checks |
| **Interrupted time series** | one series, a sharp intervention date | the pre-trend would have continued | effect at/after the break | pre-trend fit; placebo dates; seasonality handled |

## Choosing

1. Can you randomise? Do. Even a small holdout beats a large observational study.
2. Can't randomise, have a policy threshold? RDD.
3. Have groups treated at different times? DiD (use a staggered-adoption-aware estimator).
4. Have a plausible instrument? IV, and expect to defend exclusion in review.
5. One treated unit? Synthetic control.
6. Otherwise: adjustment with an explicit DAG and a sensitivity analysis. Say "assuming no unmeasured confounding" in the headline.

## Estimand first

ATE (everyone), ATT (the treated), LATE (compliers), CATE (by subgroup). Different strategies identify different estimands; don't compare a LATE to an ATE as if they were the same number.
