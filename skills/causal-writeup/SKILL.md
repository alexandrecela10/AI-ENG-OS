---
name: causal-writeup
description: Write the causal analysis writeup with the assumption in the headline, effect with CI, checks table, sensitivity verdict, alternative explanations, scope of the estimand, and the decision. Causal pack.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/causal-writeup outputs/experiments/2026-09-10-causal-summariser-ttr/
/causal-writeup --audience exec        → half-page version in plain language
/causal-writeup --review               → causal-skeptic + statistician pass before saving
```

**What you get:** `outputs/experiments/[id]/writeup.md` from `{ai-eng-os}/domains/causal/templates/causal-writeup-template.md`; optional exec summary; calibration line for the learning log.

**Time:** 30 minutes.

---

# /causal-writeup

## Steps

1. TL;DR in the standard sentence: effect, CI, population, "assuming [key assumption]". Then the decision.
2. Question, estimand, design, DAG summary.
3. Results table (primary, guardrails), effect over time, subgroups labelled.
4. Checks table from `checks.md`; sensitivity verdict from `sensitivity.md`.
5. Alternative explanations from `causal-pitfalls.md`: applied, ruled out, remaining.
6. Scope: who the estimand covers, extrapolation limits, what would change our mind.
7. Decision per the pre-registered rule; note any deviation from plan.
8. `--review`: `causal-skeptic.md` and `statistician.md`; address findings in the text.
9. Hold to `{ai-eng-os}/rubrics/writeup-standard.md`; voice `{ai-eng-os}/voice/writing-style-research.md`.

## Rules

- "Associated with" until the design earns "caused".
- The key assumption is in the first sentence, not the appendix.
- Exec version translates the CI to plain language and keeps the caveat.
