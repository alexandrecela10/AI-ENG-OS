---
name: stats-multiple-comparisons
description: Handle many metrics, slices or variants honestly: count the comparisons, choose a correction (Bonferroni, Holm, BH-FDR) or a hierarchical testing plan, and label exploratory results. Stats pack.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/stats-multiple-comparisons outputs/experiments/2026-09-03-v5/report.md
/stats-multiple-comparisons --k 24 --method holm
/stats-multiple-comparisons --best-of 8                       → correcting for picking the best variant
```

**What you get:** inline or `outputs/stats/multiplicity-[slug].md`: the count of comparisons actually made (metrics × slices × variants × looks), corrected thresholds or adjusted CIs, which results survive, which become exploratory, and the wording for the writeup.

**Time:** 10 minutes.

---

# /stats-multiple-comparisons

## Steps

1. Count honestly: primary metrics, guardrails, slices, variants tried, interim looks. The number is usually larger than the author thinks.
2. Choose: Bonferroni/Holm for a few confirmatory tests; Benjamini-Hochberg FDR for many exploratory slices; hierarchical (gatekeeping) when there's a clear primary; for best-of-k variant selection, confirm the winner on a fresh (golden) run.
3. Apply; report which findings survive, and widen CIs accordingly where you report CIs.
4. Label everything else "exploratory; needs confirmation".
5. Suggest the pre-registration for next time: one primary, listed guardrails, capped slices.

## Rules

- "We looked at 20 slices and one moved" is a hypothesis, not a result.
- Best-of-k dev-set winners are confirmed on golden once before being called wins.
