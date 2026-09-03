---
name: causal-identification
description: Choose and justify the identification strategy (RCT, DiD, IV, RDD, synthetic control, matching/adjustment) from the DAG and data situation; state the key assumption in plain words and the checks required. Produces the pre-registered analysis plan. Causal pack.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/causal-identification outputs/causal/summariser-ttr-dag.md
/causal-identification --data "staggered rollout by team over 8 weeks"
```

**What you get:** `outputs/causal/[slug]-analysis-plan.md` from `{ai-eng-os}/domains/causal/templates/causal-analysis-plan-template.md`: strategy with justification, estimand it identifies, key assumption, most plausible violation, required checks, sensitivity analyses, decision rule, power note.

**Time:** 45 minutes.

---

# /causal-identification

Reference `{ai-eng-os}/domains/causal/frameworks/identification-strategies.md` and `assumption-checks.md`.

## Steps

1. Can you still randomise (even a small holdout)? Recommend it first.
2. Match the data situation to strategies; for each viable one, state the key assumption in one plain sentence and the most plausible violation here.
3. Pick; explain why not the others.
4. Estimand identified (and whether it's the one the question asked for).
5. Required checks and sensitivity analyses for this strategy.
6. Power for the minimum effect of interest → `/stats-power`.
7. Decision rule, pre-registered. Freeze the plan (date, hash) before looking at outcomes.

## Rules

- The key assumption goes in the headline of every downstream writeup.
- If no strategy's assumption is defensible, say "not identifiable with this data" and propose the experiment that would be.
