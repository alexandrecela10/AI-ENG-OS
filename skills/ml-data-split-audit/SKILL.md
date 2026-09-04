---
name: ml-data-split-audit
description: Audit train/val/test splits and features for leakage using the leakage checklist. Checks split unit, duplicates, temporal and group leakage, target proxies, and overlap with LLM golden sets. ML pack.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/ml-data-split-audit data/splits/                    → audit existing splits
/ml-data-split-audit --propose --unit time           → propose a split scheme
/ml-data-split-audit --features features.yaml        → feature-level leakage review
```

**What you get:** `outputs/ml/split-audit-[date].md`: checklist results (pass/fail/unknown per item), counts (cross-split dups, users in both, future-dated features), suspicious features with reasons, shuffle-label sanity result if run, and a corrected split proposal.

**Time:** 45 minutes.

---

# /ml-data-split-audit

Walk `{ai-eng-os}/domains/ml/frameworks/leakage-checklist.md`. Compute what can be computed; ask for what can't.

## Steps

1. Split unit vs deployment reality (time / user / group). Mismatch = blocking.
2. Cross-split exact and near-duplicate counts; entity overlap counts.
3. Feature timing: for each feature, "is it knowable at prediction time?" Flag future aggregates and label proxies.
4. Pipeline check: preprocessing fitted on train only?
5. Test-set touch log: how many times has test been evaluated?
6. Overlap with `context-library/evals/` golden sets (hash).
7. Sanity: propose the shuffle-label and reverse-time checks; run if the harness exists.

## Rules

- Any leakage finding blocks reporting test results as evidence.
- Test set hash recorded in the report and the manifest.
