---
name: baseline
description: Establish the first number before any change: the current system, the simplest alternative (rule, retrieval-only, majority class), and the raw model with a minimal prompt, all on the same eval with CIs, cost and latency.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/baseline outputs/evals/refusal-spec-v1.md          → run the baselines the spec calls for
/baseline --include trivial,current,raw-model
/baseline --model claude-haiku-4-5                   → add a cheap-model baseline
```

**What you get:** `outputs/experiments/[date]-baseline-[name]/` with a manifest per baseline run, a `report.md` comparing them (metric with CI, cost per 1k, p95, cost per correct answer), and the baseline table copied into the eval spec.

**Time:** 30 minutes once the harness runs.

---

# /baseline

Every experiment needs something to be compared to. A good baseline set is at least three numbers.

## The three baselines

| Baseline | Why |
|---|---|
| **Trivial** | majority class, "always decline", copy the input, keyword rule. If the model doesn't beat this by a lot, stop. |
| **Current** | what's in production today (or the manual process, measured on a sample). This is what you have to beat. |
| **Raw model, minimal prompt** | the model with a one-line instruction. Shows how much the prompt engineering is worth. |

Add a **cheap model** baseline when cost matters. Add **retrieval-only** (no generation) for RAG.

## Steps

1. Confirm the harness runs (`/eval-build`) and the dataset is frozen (hash).
2. Run each baseline on the full dev set and, once, on golden. Temperature 0, 3 repeats if any sampling.
3. One manifest per run. Fill hypothesis as "baseline: [name]".
4. Report table with CIs, cost/1k, p95, cost per correct.
5. Write the baseline rows into the eval spec and note the run ids as the reference baseline for `/eval-run-report`.

## Report

```
| Baseline | pass rate | CI95 | n | $/1k | p95 ms | $/correct |
|---|---|---|---|---|---|---|
| trivial: always answer | 0.52 | 0.47–0.57 | 412 | 0 | 0 | 0 |
| current prod (v3) | 0.81 | 0.77–0.85 | 412 | 3.10 | 2810 | 3.83 |
| raw sonnet, 1-line prompt | 0.74 | 0.70–0.78 | 412 | 2.20 | 1900 | 2.97 |
| haiku, prod prompt | 0.76 | 0.72–0.80 | 412 | 0.60 | 900 | 0.79 |

Reference baseline for experiments: 2026-09-03-baseline-current.
Observation: haiku is 5 pts behind at 1/5 the cost. Worth a routing experiment.
```

## Rules

- Never start iterating before this table exists.
- Baselines are re-run when the dataset, grader or model snapshot changes.
- Include the trivial baseline even if it's embarrassing. Especially then.
