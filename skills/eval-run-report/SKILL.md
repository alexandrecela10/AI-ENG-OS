---
name: eval-run-report
description: Turn a completed eval run (or a pair of runs) into a results report with paired deltas, confidence intervals, per-slice tables, cost and latency, and a filled manifest.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/eval-run-report outputs/experiments/2026-09-03-v4/                    → single run vs the baseline in its manifest
/eval-run-report --baseline outputs/experiments/2026-08-28-v3/ --candidate outputs/experiments/2026-09-03-v4/
/eval-run-report --slices lang,difficulty
```

**What you get:** `outputs/experiments/[id]/report.md` with the results table (metric, baseline, candidate, delta, CI on delta, n, verdict), per-slice table, cost and latency, 10 wins and 10 losses with trace links, and a completed `manifest.json` (results, delta, decision left for you).

**Time:** 10 minutes.

---

# /eval-run-report

Numbers without uncertainty are anecdotes. This skill adds the uncertainty and the slices, then makes you look at the traces.

## Steps

1. **Load** `results.jsonl` and `summary.json` for baseline and candidate. Check they're on the same dataset hash; if not, stop and say so (unpaired comparisons are a different, weaker analysis).
2. **Paired deltas.** For each metric: delta = mean(candidate − baseline) per item, bootstrap 95% CI (`stats.paired_delta_ci`). Verdict per metric: outside CI (real), inside CI (no evidence), or below floor (gated failure).
3. **Slices.** Same table per slice. Flag any slice that moved the opposite way from the aggregate.
4. **Cost and latency.** Side by side. Compute cost per correct answer.
5. **Traces.** Items that flipped fail→pass (10) and pass→fail (10), with ids and trace links. Read them. Name the failure modes involved.
6. **Multiple comparisons.** If k metrics or variants, say so and apply or flag correction (`/stats-multiple-comparisons`).
7. **Fill the manifest** results block. Leave `decision` for the engineer, but recommend one.

## Report format

```
## Results: v4 vs v3 (paired, n = 412, golden refusal-v3 sha 9f2c…)

| Metric | v3 | v4 | Δ | CI95(Δ) | Verdict |
|---|---|---|---|---|---|
| refusal precision | 0.81 | 0.91 | +0.10 | [+0.06, +0.14] | real |
| task accuracy | 0.874 | 0.869 | −0.005 | [−0.02, +0.01] | no evidence |

Cost/1k: $3.10 → $3.42 (+10%). p95: 2,810 → 2,980 ms. Cost per correct: $3.55 → $3.94.

Slices: lang=fr precision +0.02 [−0.05, +0.09] (no evidence); difficulty=hard +0.15 (real).
Flipped pass→fail (8): 6 are FM-004 over-refusal on medical-adjacent benign asks. Traces: …

Recommendation: iterate. The precision gain is real; over-refusal on FM-004 needs one more example before promotion.
```

## Rules

- Never report a delta without its CI.
- Never compare runs on different item sets as if paired.
- Always show the slice that got worse.
- Hand off to `/experiment-writeup` for the narrative and `/eval-review` before any promotion decision.
