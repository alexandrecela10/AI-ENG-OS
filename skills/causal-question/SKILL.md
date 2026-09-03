---
name: causal-question
description: Turn a business question ("did the new prompt reduce churn?") into a precise causal question with treatment, outcome, population, comparison, estimand and the decision it drives. Causal pack.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/causal-question "did the AI summariser reduce time-to-resolution?"
/causal-question --from outputs/reports/rollout-summariser-v5.md
```

**What you get:** `outputs/causal/[slug]-question.md`: the causal question in the standard form, estimand with justification, decision rule, smallest effect worth acting on, and whether this is answerable with the data at hand (or needs an experiment). Seeds `templates/causal-analysis-plan-template.md`.

**Time:** 20 minutes.

---

# /causal-question

## Clarify

```
1. What decision depends on the answer? What would you do differently at effect = 0 vs effect = X?
2. Treatment: exactly what, for whom, starting when? Was it assigned, chosen, or rolled out?
3. Outcome: exactly what, measured when, over what window?
4. Compared to what? (nothing / old version / never-treated)
5. Population you care about: everyone, the treated, those who'd comply?
6. Smallest effect worth acting on?
```

## Write

"What is the effect of [X] on [Y] for [population], compared to [control], measured at [time]?" Estimand (ATE/ATT/LATE/CATE) with why. Decision rule. Minimum effect of interest. Data situation → hint at strategy (`/causal-identification`). Confounders you can already name → `/causal-dag`.

## Rules

- If the question is predictive ("who will churn"), route to `/ml-problem-framing`.
- If it's descriptive ("how much did churn change"), say so; that's not causal.
- "Did users who used X do better" is a correlation question until the design makes it causal.
