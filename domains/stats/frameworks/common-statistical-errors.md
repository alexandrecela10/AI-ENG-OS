# Common Statistical Errors

What `/stats-result-check` and the `statistician` persona look for first. Each with the fix.

| Error | How it shows up | Fix |
|---|---|---|
| **Unpaired analysis of paired data** | two systems on the same 400 items compared as if 800 independent samples | per-item differences; bootstrap CI on the mean difference |
| **Wrong unit of analysis** | requests analysed as independent when users generate many | aggregate or cluster by user; effective n is users |
| **Underpowered, then "no effect"** | n = 40, CI spans −10 to +12 pts, conclusion "no difference" | "no evidence at this n"; report the detectable effect; `/stats-power` |
| **Peeking / optional stopping** | check daily, stop when p < 0.05 | pre-register duration or use sequential methods |
| **Garden of forking paths** | 12 metrics × 4 slices, one is significant | pre-register primary; correct; label exploratory |
| **Best-of-k reported as one** | tried 8 prompt variants, reported the winner's dev score | confirm on golden once; correct for selection |
| **Regression to the mean** | "worst slice improved after we fixed it" | control comparison; expect part of the bounce |
| **Simpson's paradox** | aggregate up, every slice down (mix shift) | stratify; weight consistently |
| **Survivorship / selection** | metric computed on completed sessions only | define population before outcome |
| **Confusing SE and SD** | error bars that shrink with n but described as spread, or vice versa | label; CIs on estimates, SD for spread |
| **p-value as effect size** | "highly significant" for a 0.2 pt change at n = 100k | report the effect with CI; ask if it matters |
| **Accepting the null** | "not significant, so equal" | equivalence test or CI within a pre-set margin |
| **Non-determinism ignored** | single run at temperature 0.7 | repeats; between-run sd; or temp 0 with seed |
| **Ordinal treated as interval** | mean of 1–5 rubric scores compared with a t-test | distribution, share ≥ 4, Wilcoxon / ordinal model |
| **Heavy-tailed mean** | mean latency moved by two outliers | medians / percentiles with bootstrap CIs; log scale |
| **Base-rate neglect** | 95% precision on a 0.1% positive class assumed fine | precision at the deployment prevalence; PR curve |
| **Post-hoc power** | "power was 0.9 for the effect we found" | power for the pre-specified effect of interest only |

## Quick triage questions

What's the unit? Paired or not? How many looks, metrics, variants? What's the CI on the difference? Was the effect size fixed before the data?
