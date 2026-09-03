---
name: data-quality-audit
description: Audit a dataset for duplicates, leakage, label noise, PII, representativeness and drift, using {ai-eng-os}/scaffolds/data-pipeline and the data quality rubric. Produces findings and a cleaning plan.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/data-quality-audit data/train.jsonl
/data-quality-audit data/train.jsonl --against evals/golden/*.jsonl      → leakage check vs golden sets
/data-quality-audit --run-pipeline                                        → copy and run the pipeline scaffold, report counts
```

**What you get:** `outputs/datasets/audit-[name]-[date].md`: rubric scores, findings ranked by severity, counts (dups, near-dups, PII hits, leakage overlaps), 50-row human read notes, and a cleaning plan with expected row loss.

**Time:** 45 minutes.

---

# /data-quality-audit

## Steps

1. **Counts.** Rows, exact dups, near-dups (shingle Jaccard ≥ 0.9, or the project's method), PII hits by type, length outliers.
2. **Leakage.** Overlap with every golden/dev set (ids, exact content, near-dup). Temporal leakage if there's a time field. Group leakage if there's a user/entity field.
3. **Labels.** Distribution; by labeller/date if available; sample 50 for a human read, note disagreements.
4. **Representativeness.** Slice distribution vs production (from traces or the brief).
5. **Rubric.** Score all 8 dimensions of `{ai-eng-os}/frameworks/data-quality-rubric.md`.
6. **Plan.** Ordered cleaning steps with expected row loss; which steps the pipeline scaffold covers; what needs a proper tool (PII detector, MinHash at scale).
7. `--run-pipeline`: copy `{ai-eng-os}/scaffolds/data-pipeline/` to `outputs/scaffolds/data-pipeline/`, run it, attach the report.

## Rules

- Any leakage with a golden set is a blocking finding.
- Report counts in → out at each step.
- Read the rows. Fifty, by hand.
