# Eval Spec: [name]

**Owner:** [name] · **Version:** v1 · **Gated:** yes / no · **Status:** Draft / Frozen

## What this eval measures

One sentence on the capability or behavior. One sentence on what it deliberately does not measure.

**Eval type:** capability / behavior / safety / regression (see `{ai-eng-os}/frameworks/eval-taxonomy.md`)

## Task definition

- **Input:** [schema, example]
- **Expected output:** [schema, example]
- **Edge cases that must be represented:** [list, with target share of the set]

## Dataset

- **Source:** [production sample / hand-written / synthetic / public benchmark]. Provenance and licence.
- **Size:** n = [ ]. Power note: to detect a [X] pt change at 95% CI you need roughly n = [ ] (see `/stats-power`).
- **Split:** golden (frozen, for gating) / dev (for iteration). Never iterate against golden.
- **Contamination check:** [how you verified the model hasn't seen these items]
- **Refresh policy:** [when items rotate, who approves]

## Grading

- **Grader:** exact match / code check / LLM judge with rubric / human
- **Rubric:** `rubrics/[name].md` (for LLM judges). Judge model: [ ]. Calibration: agreement with humans = [κ or %] on n = [ ] (`/judge-calibrate`).
- **Metric(s):** [accuracy, F1, pass@k, refusal precision/recall, hallucination rate, cost per correct answer]
- **Aggregation:** [per-item mean; report 95% CI via bootstrap]

## Baseline

| Run | Metric | Value | CI95 | n | Cost / 1k | p95 ms |
|---|---|---|---|---|---|---|
| [current prod] | | | | | | |

## Pass / fail thresholds (for gated evals)

- Ship if: [metric] >= [floor] and no gated metric drops by more than its CI.
- Stop if: [condition].

## Known weaknesses of this eval

Goodhart risks, judge biases (length, position, self-preference), coverage gaps.
