---
name: stats-test-select
description: Pick the right test and CI method for a comparison from the outcome type, design and unit of analysis; check assumptions; write the analysis plan lines. Stats pack.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/stats-test-select "compare v4 vs v5 pass rate on the same 412 items"
/stats-test-select "p95 latency across three models, 3 runs each"
/stats-test-select --plan outputs/stats/analysis-plan-[slug].md      → fill the Analysis section
```

**What you get:** inline recommendation (test, CI method, unit, assumptions to check, code sketch using the harness or repo libraries), and on request an `outputs/stats/analysis-plan-[slug].md` from `{ai-eng-os}/domains/stats/templates/analysis-plan-template.md`.

**Time:** 10 minutes.

---

# /stats-test-select

Reference `{ai-eng-os}/domains/stats/frameworks/test-selection-guide.md`.

## Steps

1. Outcome type (binary / continuous / skewed / ordinal / count / time-to-event).
2. Design: paired (same items) or independent; >2 groups; clustering (users, sessions, documents); repeats.
3. Unit of analysis and effective n.
4. Test + CI method from the table. Default to bootstrap CIs on the effect; add the test if a p-value is wanted.
5. Assumptions to check, with what to do if violated.
6. Code sketch (`stats.paired_delta_ci`, `wilson`, or the repo's stats library).

## Rules

- Paired data gets a paired analysis. Always.
- Report the CI on the difference; the p-value is secondary.
- Ordinal rubric scores are not means.
