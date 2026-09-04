---
name: dataset-card
description: Write a dataset card (provenance, composition, labels, splits, leakage checks, quality score, licence) for any eval set, training set or retrieval corpus.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/dataset-card evals/golden/refusal-v3.jsonl
/dataset-card --from-report outputs/reports/pipeline-report.json      → use the data-pipeline report for counts
```

**What you get:** `outputs/datasets/[name]-card-v[n].md` from `{ai-eng-os}/templates/dataset-card-template.md`, with the sha256, slice counts computed from the file, and the quality rubric scored.

**Time:** 20 minutes.

---

# /dataset-card

## Steps

1. Compute: row count, sha256, slice counts, length p5/p50/p95, exact-dup count. Use the data-pipeline report if provided.
2. Ask for what can't be computed: source, collection window, consent/PII handling, labellers and agreement, licence, intended and prohibited use.
3. Run leakage checks against every set in `context-library/evals/` (id and content hash overlap) and report.
4. Score `{ai-eng-os}/frameworks/data-quality-rubric.md`; name the two weakest dimensions.
5. Fill the template. Save. Offer to add the sha to `context-library/evals/README.md` when promoted.

## Rules

- No card without a hash.
- Say "unknown" rather than guessing provenance.
- Any rubric dimension at ≤2 gets a warning at the top of the card.
