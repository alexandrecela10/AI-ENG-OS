---
name: golden-set-curate
description: Build or extend a golden eval set from traces, tickets and failure modes. Stratified by slice, contamination-checked, frozen with a hash, and separated from the dev set.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/golden-set-curate outputs/evals/refusal-spec-v1.md        → build items to the spec's slice targets
/golden-set-curate --from outputs/traces/2026-08/ --n 400  → sample and label from traces
/golden-set-curate --add-regression FM-007                  → add cases for a failure mode
/golden-set-curate --refresh 10%                           → rotate items (approval required)
```

**What you get:** `outputs/evals/[name]-golden-v[n].jsonl` and `[name]-dev-v[n].jsonl` in the harness schema, a `README` with provenance, slice counts, contamination checks and the sha256, and a list of items that need human labels.

**Time:** 1–3 hours for a first set of 300–500 items.

---

# /golden-set-curate

The golden set is the most valuable artefact in the project. It's frozen, it gates releases, and it grows one regression case at a time.

## Context routing

| Source | Use |
|---|---|
| eval spec | slice targets, grader (decides what "expected" looks like) |
| `outputs/traces/`, logs, support tickets | real inputs |
| `context-library/failure-modes.md` | every open FM → at least 5 items tagged with its id |
| `context-library/evals/` | existing sets; don't duplicate items; check overlap |
| `{ai-eng-os}/frameworks/data-quality-rubric.md` | quality checks |

## Steps

1. **Target table.** From the spec: slice × count. Add: 10% adversarial / off-distribution, 5% "answer not available" (should decline), regression cases for each open FM.
2. **Source items.** Prefer real inputs, de-identified (`{ai-eng-os}/scaffolds/data-pipeline/` scrub step). Hand-write only for slices with no real data; mark `source: handwritten`. Synthetic generation is fine for adversarial slices; mark the generator.
3. **Write expected outputs** in the grader's form. For LLM-judge items, write the reference or checklist, not a full gold answer.
4. **Label quality.** Anything gated: two labellers on a 20% sample, report agreement. Flag items with disagreement for adjudication.
5. **Contamination check.** Search 10 random items verbatim on the web; hash-check against fine-tuning data and other eval sets; near-dup check within the set.
6. **Split.** 70% golden / 30% dev, stratified. Golden is frozen: compute sha256, write it in the README and in `context-library/evals/README.md` once promoted.
7. **Report** slice counts vs targets, contamination results, labeller agreement, items needing human review.

## Rules

- Never put dev items in golden or vice versa. Same `id` prefix scheme, different files.
- Never edit a golden item in place; refresh creates v+1 and records what changed and why. Refresh needs approval from a name in `stakeholders.md`.
- Every regression case carries the FM id in `tags`.
- Small honest set beats a large noisy one. 300 clean items with CIs beat 3,000 unlabelled.
