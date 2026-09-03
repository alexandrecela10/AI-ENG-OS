---
name: ml-ablation
description: Design and report ablations that isolate what actually helped: one component per row, seeds, CIs on the delta, cost, and a keep/drop decision. ML pack.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/ml-ablation --base outputs/experiments/2026-09-05-gbm-v3/ --components "feature-group-text,target-encoding,class-weights"
/ml-ablation --report outputs/experiments/2026-09-06-ablations/
```

**What you get:** an ablation plan, then `outputs/ml/ablation-[slug].md` from `{ai-eng-os}/domains/ml/templates/ablation-table-template.md` with the table, the reading, and the final configuration.

**Time:** 20 minutes to plan; runs vary.

---

# /ml-ablation

## Steps

1. Base configuration = current best, with its manifest.
2. One row per component: remove it (or add the candidate technique), everything else fixed, same seeds, same budget.
3. Delta vs base with a CI over seeds (paired by seed where possible).
4. Keep components whose removal hurts beyond the CI; drop the rest (simpler ships).
5. Note interactions worth a follow-up; don't test them in this table.
6. Manifest per row.

## Rules

- One change per row.
- A component that "should help" but doesn't beyond the CI gets dropped.
- Report cost/latency per row; sometimes the ablation is a speedup.
