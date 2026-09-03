---
name: eval-review
description: Adversarial review of an eval result using the eval-skeptic persona and the eval validity checklist. Verdict is evidence / weak evidence / not evidence yet, with the smallest run that would settle it.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/eval-review outputs/experiments/2026-09-03-v4/          → review a run's report and manifest
/eval-review outputs/evals/refusal-spec-v1.md           → review a spec before building it
/eval-review --panel                                      → add statistician and research-scientist personas
```

**What you get:** `outputs/experiments/[id]/review.md` (or `outputs/evals/[name]-spec-review.md`): checklist results, verdict, top three unanswered questions, recommended follow-up run.

**Time:** 15 minutes.

---

# /eval-review

Run before any promotion decision and before any number goes into a status update.

## Method

1. Adopt `{ai-eng-os}/agents/eval-skeptic.md`. With `--panel`, also `statistician.md` and `research-scientist.md`; synthesise and flag disagreements.
2. Walk `{ai-eng-os}/frameworks/eval-validity-checklist.md` section by section against the manifest, report and spec. Mark each item pass / fail / unknown with a one-line reason.
3. Look for the classic lies (`{ai-eng-os}/frameworks/experiment-discipline.md` § Common ways experiments lie).
4. Verdict:
   - **Evidence**: all critical items pass; delta outside CI on the primary metric; no gated metric below floor.
   - **Weak evidence**: passes but with caveats (small n, uncalibrated judge, single run at temp > 0).
   - **Not evidence yet**: any of contamination unknown, dev/golden mixed, unpaired comparison, delta inside CI, judge uncalibrated on a gated metric.
5. Prescribe the smallest additional run or check that would move the verdict up one level.

## Output

```
## Eval review: 2026-09-03-v4

Construct validity: pass (metric maps to refusal complaints in support tickets)
Contamination: UNKNOWN – no search or hash check recorded
Judge: pass (κ 0.71, calibrated 2026-08-30)
Statistics: pass (paired, n=412, CI reported)
Operational: pass

Verdict: weak evidence.
Top questions: (1) were any golden items in the few-shot examples added in v4? (2) 3 repeats or temp 0? (3) FM-004 regression: is it inside CI per slice?
Smallest next step: hash-check v4 few-shots against golden ids; re-run FM-004 slice with n≥100.
```

## Rules

- Be specific. "Sample size may be small" is not a finding; "n=42 on the fr slice gives a ±15 pt CI" is.
- A failed critical check means the number is not evidence, however good it looks.
- Record the verdict in the manifest under `review`.
