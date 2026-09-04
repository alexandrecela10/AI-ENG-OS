# Causal Pitfalls

The alternative explanations a causal skeptic reaches for first. Address each explicitly in the writeup or accept the softened claim.

| Pitfall | What it looks like | What to do |
|---|---|---|
| **Confounding** | a third variable drives both X and Y (heavier users adopt the feature and also retain) | DAG; adjust for the set that blocks back-door paths; sensitivity analysis |
| **Selection bias** | who ends up in the sample depends on X and Y (survivors only) | draw selection as a node; condition on it only if it's not a collider |
| **Collider bias** | adjusting for something caused by both X and Y creates a spurious link | check every adjustment variable against the DAG |
| **Reverse causation** | Y causes X (churn-prone users stop using the feature) | timing: X measured before Y; use lagged designs |
| **Mediator adjustment** | controlling for the mechanism erases the effect | don't adjust for descendants of X unless you want the direct effect |
| **Interference / spillover** | one unit's treatment affects another's outcome (marketplaces, social features) | cluster randomisation; switchback; state SUTVA violation risk |
| **Sample-ratio mismatch** | randomisation didn't produce the intended split | SRM test before reading results; investigate, don't analyse |
| **Novelty / learning effects** | early effect fades or grows | longer window; plot effect over time |
| **Peeking / optional stopping** | checking daily and stopping when significant | pre-register duration; sequential methods if you must peek |
| **Multiple outcomes / subgroups** | one of twenty is significant | pre-register primary; correct or label exploratory (`/stats-multiple-comparisons`) |
| **Measurement error in treatment** | logged exposure ≠ actual exposure | intent-to-treat; instrument with assignment |
| **Regression to the mean** | "worst performers improved after intervention" | control group or pre-trend |
| **Simpson's paradox** | aggregate effect reverses within strata | stratify; check heterogeneity |
| **Extrapolation** | LATE for compliers presented as the effect on everyone | name the population the estimand covers |

## The one-line test

"If X had not happened, would Y have been different?" If you can't say what the counterfactual is and how you approximate it, you don't have a causal estimate yet.
