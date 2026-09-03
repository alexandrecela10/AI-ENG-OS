---
name: stats-power
description: Power and sample-size analysis for an eval, A/B test or causal study: required n for the minimum effect worth detecting, or detectable effect at the n you have, with paired/clustered designs handled by simulation. Stats pack.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/stats-power --baseline 0.81 --mde 0.03 --paired --disagreement 0.15
/stats-power outputs/evals/refusal-spec-v1.md                → pull baseline and MDE from the spec
/stats-power --have-n 412                                     → detectable effect at this n
```

**What you get:** `outputs/stats/power-[slug].md` from `{ai-eng-os}/domains/stats/templates/power-analysis-template.md`, with the number, a sensitivity table, and a recommendation. For paired binary, ordinal or clustered designs, a short simulation script in the repo's language and the result.

**Time:** 15 minutes.

---

# /stats-power

## Steps

1. Inputs: outcome type, design (paired items / independent / clustered), baseline, variability (sd; or for paired binary the per-item disagreement rate, which drives power far more than the baseline rate), MDE from the decision rule, α, power, number of primary comparisons.
2. Method: closed form for simple cases; simulation for paired binary (McNemar-type), ordinal, clustered, or anything with repeats.
3. Output: required n, or detectable effect at available n; sensitivity to variability.
4. Recommendation: proceed / more items / pair the design / cut metrics / label exploratory.

## Rules of thumb to quote

Binary pass rate near 0.8: n = 400 → ±4 pts CI; n = 1,000 → ±2.5. Paired delta of 3 pts with 15% item disagreement: n ≈ 500–600 at 80% power. These are starting points; run the numbers.

## Rules

- MDE comes from the decision, not from what's convenient.
- Correct α for the number of primary comparisons before computing n.
- Never compute post-hoc power for the effect you found.
