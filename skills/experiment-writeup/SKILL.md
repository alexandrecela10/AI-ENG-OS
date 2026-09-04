---
name: experiment-writeup
description: Write the experiment writeup from a manifest and report: TL;DR, hypothesis vs result, setup, results with CIs, where it hurt, threats to validity, decision, calibration note. Held to the writeup standard.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/experiment-writeup outputs/experiments/2026-09-03-v5/
/experiment-writeup outputs/experiments/2026-09-03-v5/ --audience exec     → half-page version too
/experiment-writeup --review                                                → research-scientist pass before saving
```

**What you get:** `outputs/experiments/[id]/writeup.md` from `{ai-eng-os}/templates/experiment-writeup-template.md` in `{ai-eng-os}/voice/writing-style-research.md` voice; optional exec summary; a calibration line offered for the learning log.

**Time:** 20 minutes.

---

# /experiment-writeup

Discarded experiments get written up too. They're the ones people repeat.

## Steps

1. **Read** manifest, report, review (if any). If the report lacks paired CIs, run `/eval-run-report` first.
2. **TL;DR** in three sentences: change, effect with CI, next step.
3. **Hypothesis** with the predicted number beside the actual.
4. **Setup**: one variable, tuple with versions, baseline run id, what was held fixed.
5. **Results** table: every gated metric, baseline, run, delta, CI(delta), n, verdict. Cost and p95 line.
6. **Where it hurt**: the worst slice; 3–5 trace links; failure modes that changed.
7. **Threats to validity**: address each from the checklist that applies.
8. **Decision and next**: promote/iterate/discard; the next single-variable experiment.
9. **Calibration**: predicted vs actual by change type; offer to append to `context-library/ai-eng-os-learning-log.md`.
10. **Check** against `{ai-eng-os}/rubrics/writeup-standard.md`; `--review` adopts `research-scientist.md`.

## Rules

- No "significantly" without a test. No delta inside its CI called an improvement.
- Two pages, then appendix.
- The writeup is the memory of the team; write it the same day.
