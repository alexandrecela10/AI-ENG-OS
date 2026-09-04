---
name: causal-sensitivity
description: Stress-test a causal estimate: sensitivity to unmeasured confounding, alternative specifications and adjustment sets, placebo tests, bandwidth or donor variations, and a robustness verdict. Causal pack.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/causal-sensitivity outputs/experiments/2026-09-10-causal-summariser-ttr/
/causal-sensitivity --evalue --placebo-dates 3 --alt-specs 2
```

**What you get:** `outputs/experiments/[id]/sensitivity.md`: table of analyses (what varied, effect, CI), the confounding strength needed to nullify the effect (E-value / Rosenbaum / coefficient stability), placebo results, and a verdict: robust / fragile / not robust, with the sentence to use in the writeup.

**Time:** 30–60 minutes.

---

# /causal-sensitivity

## Analyses by strategy

- All: alternative adjustment sets from the DAG; leave-one-covariate-out; effect on a placebo outcome that X shouldn't affect.
- Adjustment/matching: E-value or Rosenbaum bounds; doubly robust vs single spec.
- DiD: placebo dates; alternative control groups; estimator comparison under staggered adoption.
- RDD: bandwidth sweep; polynomial order; placebo cutoffs; donut.
- IV: alternative instruments if any; over-identification if applicable; LATE vs OLS comparison discussed.
- Synthetic control: in-space and in-time placebos; leave-one-donor-out; permutation p.

## Verdict

**Robust**: sign and rough magnitude stable across all; nullifying confounder would need to be implausibly strong. **Fragile**: sign stable, magnitude moves beyond CI in some specs. **Not robust**: sign flips or effect vanishes under a plausible spec. Write the one-sentence caveat for the TL;DR.

## Rules

- Report every analysis run, not the favourable ones.
- Adopt `causal-skeptic.md` and answer its top alternative explanation explicitly.
