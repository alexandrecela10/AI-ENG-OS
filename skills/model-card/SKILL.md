---
name: model-card
description: Write or update the model / system card for a release: what it is, eval results with CIs, safety summary, limitations, data, monitoring, change log.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/model-card --release v5
/model-card --update outputs/reports/model-card-v4.md --with outputs/experiments/2026-09-03-v5/
```

**What you get:** `outputs/reports/model-card-[system]-v[n].md` from `{ai-eng-os}/templates/model-card-template.md`, numbers pulled from manifests, safety from the latest red-team and safety review, limitations from `failure-modes.md`.

**Time:** 30 minutes.

---

# /model-card

## Steps

1. Gather: brief, latest candidate manifests (capability, safety, regression), red-team report, safety review, dataset cards, rollout plan, failure-modes.
2. Fill every section. Where a number is missing, write "not measured" rather than omitting the row.
3. Limitations: top failure modes by frequency on golden, with the mitigation and status.
4. Change log: what changed since the last card, with eval deltas.
5. Save; hand to `/launch-readiness`.

## Rules

- Every number has n and CI.
- Intended use and out-of-scope use are both filled.
- Approvers named from `stakeholders.md`.
