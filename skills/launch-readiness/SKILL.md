---
name: launch-readiness
description: Assemble the launch readiness review for a release: gated evals, eval validity, safety, regression, cost, latency, tracing, monitoring, rollback, rollout plan, docs. Stops at the human gate.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/launch-readiness --release v5
/launch-readiness --panel            → add infra-reviewer, safety-reviewer, ops-reviewer, user-advocate notes
```

**What you get:** `outputs/reports/launch-readiness-[system]-v[n].md` from `{ai-eng-os}/templates/launch-readiness-template.md`, each gate marked with evidence links, accepted risks, conditions, and a sign-off table for the named approvers. No "GO" is written by this skill; the humans write it.

**Time:** 30–45 minutes.

---

# /launch-readiness

## Steps

1. **Gather** candidate manifests, `/eval-review` verdict, red-team report, `/safety-review`, regression + jailbreak runs, cost/latency report, tracing and dashboard links, rollback test date, `/rollout-plan`, model card, changelog draft.
2. **Fill each gate** with a link and a status. Missing evidence = ☐, not ☑.
3. **Accepted risks** table with owners.
4. **Conditions** for a GO-with-conditions, each with owner and date.
5. **Panel** (`--panel`): `infra-reviewer`, `safety-reviewer`, `ops-reviewer`, `user-advocate` each add a short note; conflicts flagged.
6. **Sign-off table** with names from `stakeholders.md` § Launch approvers. Leave decisions blank.

## Rules

- This skill never writes GO. It presents evidence.
- An eval-review verdict of "not evidence yet" on a gated metric is a blocking gap.
- Rollback untested = not ready.
