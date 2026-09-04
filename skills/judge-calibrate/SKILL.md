---
name: judge-calibrate
description: Measure an LLM judge against human labels before trusting it. Agreement (kappa), position and length bias, self-preference, and the threshold that best matches humans.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/judge-calibrate --rubric rubrics/faithfulness-v1.md --labels evals/human-labels.jsonl
/judge-calibrate --pairwise                       → also test position-swap consistency
```

**What you get:** `outputs/evals/judge-calibration-[rubric]-[date].md`: agreement with humans (κ, %), confusion matrix, bias checks, recommended pass threshold, and a verdict on whether the judge can gate.

**Time:** 30 minutes plus the human labels (n >= 100, ideally 200).

---

# /judge-calibrate

An uncalibrated judge is an opinion with a decimal point.

## Steps

1. **Collect human labels.** n >= 100 items scored on the same rubric by 2 humans; report inter-human agreement first (that's the ceiling).
2. **Run the judge** on the same items, temperature 0, pinned snapshot, 3 repeats to measure self-consistency.
3. **Agreement.** Cohen's κ (or weighted κ for 1–5), exact and ±1 agreement, confusion matrix. Compare to the inter-human number.
4. **Bias checks.**
   - Length: correlation between response length and judge score, controlling for human score.
   - Position (pairwise): swap consistency rate.
   - Self-preference: if the judge and the system under test share a model family, compare against a different-family judge on a subsample.
   - Verbosity of reasoning: does asking for reasons change the score distribution?
5. **Threshold.** For pass/fail gating, pick the score cut that maximises agreement with human pass/fail; report precision and recall of the judge at that cut.
6. **Verdict.** Can gate (κ >= 0.7 and no bias > 0.2 correlation) / can rank but not gate / needs a better rubric. Write the improvements to the rubric if needed and bump its version.

## Report

```
Judge: claude-sonnet-4-5@2025-09-29, rubric faithfulness-v1, n = 180
Inter-human κ = 0.78. Judge–human weighted κ = 0.71 (95% CI 0.63–0.79). Exact agreement 64%, ±1 87%.
Length bias: r = 0.08 (ok). Self-consistency: 96%.
Recommended pass threshold: >= 4 (precision 0.91, recall 0.86 vs human pass).
Verdict: can gate. Record rubric sha in manifests.
```

## Rules

- Never gate a release on an uncalibrated judge.
- Re-calibrate when the rubric, judge model snapshot or task distribution changes.
- Write the calibration result into the eval spec and the manifest's grader block.
- Use `/stats-uncertainty-report` for the CI on κ if n is small.
