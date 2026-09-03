---
name: causal-estimate
description: Run the pre-registered estimation and assumption checks, producing effect estimates with CIs, balance and check tables, plots, and a manifest. Causal pack.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/causal-estimate outputs/causal/summariser-ttr-analysis-plan.md --data data/ttr.parquet
/causal-estimate --scaffold             → generate the analysis notebook/script skeleton for the chosen strategy
```

**What you get:** `outputs/experiments/[date]-causal-[slug]/` with `manifest.json` (change type `analysis`, data hash, code sha, plan hash), `results.md` (effect table with CIs, guardrails, subgroups labelled pre-specified/exploratory, effect-over-time), `checks.md` (every required check with result and verdict), and plots. With `--scaffold`, a script skeleton using the libraries already in the repo.

**Time:** varies; 30 minutes to set up.

---

# /causal-estimate

## Steps

1. Load the frozen plan; refuse to deviate without logging the deviation.
2. SRM / balance / overlap checks first. Fail → stop and report; don't estimate.
3. Estimate per plan; clustered SEs at the assignment level; CI on the effect.
4. Run every required check from `assumption-checks.md`; table with verdicts.
5. Guardrails and pre-specified subgroups. Anything else is labelled exploratory.
6. Plots: effect over time, event study / RD plot / synthetic fit as applicable.
7. Manifest and hand to `/causal-sensitivity`.

## Rules

- Checks before estimates.
- No subgroup result presented without its pre-registration status.
- Effect with CI, never a bare point estimate or a bare p-value.
