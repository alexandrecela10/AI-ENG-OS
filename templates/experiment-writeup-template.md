# [Experiment title]

**Author:** [name] · **Date:** [ ] · **Manifest:** `outputs/experiments/[id]/manifest.json` · **Decision:** promote / iterate / discard

## TL;DR

Three sentences: what we changed, what moved (with CI), what we're doing next.

## Hypothesis

"If we [change], then [metric] will [direction, magnitude] because [mechanism]." Predicted delta: [ ]. Actual: [ ].

## Setup

- **Change (one variable):** [ ]
- **Tuple:** prompt v[ ] · model [ ] · dataset [ ] (n = ) · grader [ ] · config [ ]
- **Baseline:** run [ ]
- **What we held fixed:** [ ]

## Results

| Metric | Baseline | This run | Delta | CI95 on delta | n | Verdict |
|---|---|---|---|---|---|---|
| | | | | | | outside / inside noise |

Cost: [ ] → [ ] · p95: [ ] → [ ]

## Where it helped, where it hurt

Slice table or 3–5 representative traces (links). Name the failure modes that changed frequency.

## Threats to validity

Contamination, judge bias, small n, multiple comparisons, dev/golden mixing, distribution shift. What you did about each.

## Decision and next step

What we're doing, why, and the next single-variable experiment.

## Calibration note

Predicted [ ] vs actual [ ] for change type [ ]. Logged to `context-library/ai-eng-os-learning-log.md`: yes / no.
