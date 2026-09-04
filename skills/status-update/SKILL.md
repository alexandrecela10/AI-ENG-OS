---
name: status-update
description: Weekly or milestone status for an AI engineering workstream: metric movement with uncertainty, experiments run and decided, risks, asks. Audience-aware (team, exec, cross-functional).
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/status-update                          → this week, from outputs/experiments/ and the learning log
/status-update --audience exec
/status-update --since 2026-08-25
```

**What you get:** `outputs/status-updates/[date]-[workstream].md`. Team version by default; `--audience exec` uses `{ai-eng-os}/voice/writing-style-exec.md`.

**Time:** 10 minutes.

---

# /status-update

## Gather

Manifests since the last update (decisions, deltas), open incidents, launch readiness state, red-team status, budget vs actual, blockers.

## Format (team)

```
## [workstream] — week of [date]

Headline: [metric] [from] → [to] (CI [ ]) on golden; [n] experiments, [k] promoted.
Shipped: v5 to 10% canary (promotion criteria met on day 3). Rollback tested.
Learned: [1–3 bullets, each with a number or a trace link]
Discarded: [experiments with "no evidence", so nobody repeats them]
Risks: [risk → mitigation → owner]
Next week: [next experiments, one variable each]
Asks: [specific, with a name]
```

## Format (exec)

"So what" first, one headline number with plain-language uncertainty, risk sentence, ask sentence. Half a page. Link the writeups.

## Rules

- Numbers with uncertainty, never bare.
- Discarded experiments are progress; list them.
- Every ask names a person.
