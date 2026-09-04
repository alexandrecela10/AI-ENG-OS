---
name: jailbreak-regression
description: Maintain and run the jailbreak and prompt-injection regression suite: convert new attack reports into cases, run against release candidates, gate on success rate.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/jailbreak-regression --run prompts/assistant.md@v5
/jailbreak-regression --add outputs/red-team/round-3-report.md       → convert successful attacks into cases
/jailbreak-regression --add-from-incident outputs/postmortems/2026-09-01.md
```

**What you get:** `outputs/evals/jailbreak-regression-[date].md` (attack success rate by category with CI, newly succeeding cases, verdict vs floor) and, with `--add`, new items in `outputs/evals/jailbreak-suite-v[n].jsonl` tagged by category and FM id.

**Time:** minutes to run; 15 minutes to add cases.

---

# /jailbreak-regression

## Suite shape

Items in the harness schema with `tags: ["safety", "<category>", "FM-xxx"]`, `expected` describing the acceptable behavior (decline / ignore injected instruction / ask for confirmation). Grader: LLM judge with a refusal rubric, calibrated, or code check where behavior is checkable (e.g. gated tool not called).

## Run

Temperature 0, pinned snapshot, 3 repeats (jailbreaks are often stochastic; report worst-of-3 too). Success rate per category with Wilson CI. Floor from the safety spec. Any category above floor → FAIL.

## Add

From a red-team report or postmortem: one item per successful attack class, described abstractly enough to be safe to store, concrete enough to reproduce. Never delete items.

## Rules

- Restricted access for the suite file if payloads are sensitive; note the location, not the content, in shared docs.
- Runs on every release candidate (`/prompt-regression --setup-ci` includes it).
- Model snapshot bumps re-run this suite; behavior shifts silently across snapshots.
