---
name: prompt-iterate
description: Improve a prompt one change at a time against the dev set, with a hypothesis, a manifest and a paired delta for each iteration. Confirms on golden only when a candidate is worth shipping.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/prompt-iterate prompts/summariser.md                        → propose the next single change from the latest failures
/prompt-iterate prompts/summariser.md --hypothesis "adding a decline example fixes FM-004"
/prompt-iterate --loop 3                                      → up to 3 iterations, each measured, stop early if no evidence
/prompt-iterate --candidate                                   → run the current best on golden, produce a candidate report
```

**What you get:** for each iteration a new prompt version (`v+1`), `outputs/experiments/[date]-[prompt]-v[n]/` with manifest + report, and a one-paragraph log entry. With `--candidate`, a golden run and a recommendation to promote/iterate/discard.

**Time:** 15–30 minutes per iteration once the harness runs.

---

# /prompt-iterate

## Preconditions (checked, not assumed)

- An eval spec and harness exist for this prompt (else offer `/eval-spec` / `/eval-build`).
- A baseline run exists on the current dataset hash (else `/baseline`).
- The prompt is in the registry with a pinned model snapshot.

## The iteration

1. **Read the losses.** From the latest run's `results.jsonl`, cluster the failed items (by FM tag, slice, reason). Pick the biggest cluster.
2. **Hypothesis.** "Changing [one thing] will fix [cluster] and raise [metric] by ~[x] pts, because [mechanism]." Write the predicted number down.
3. **One change.** Apply the smallest edit that tests the hypothesis (`{ai-eng-os}/frameworks/prompt-engineering-principles.md`). Bump the version; changelog line.
4. **Run on dev.** Temperature 0. Same items, same grader as the baseline.
5. **Report** via `/eval-run-report` logic: paired delta with CI on every gated metric, per slice, cost, p95. Read 5 wins and 5 losses.
6. **Decide.** Real gain on the target and no gated regression → keep, move to the next cluster. Inside CI → revert and log ("no evidence"). Gated regression → revert.
7. **Log** the calibration (predicted vs actual) to `context-library/ai-eng-os-learning-log.md` (offer, don't force).

## Candidate (`--candidate`)

Run the current best version on golden once. Run the regression suite. Produce a candidate report and hand to `/eval-review` before anyone says "promote".

## Rules

- One variable. If the user wants to change two things, do two iterations.
- Never touch golden inside the loop.
- Never delete a failed version; it's a data point.
- Stop after two consecutive "no evidence" iterations and suggest a different lever (model, retrieval, data) or a deeper `/trace-debug`.
