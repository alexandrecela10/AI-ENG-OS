---
name: changelog
description: Write the changelog entry for a model-backed release: what changed for users, eval deltas with CIs, cost and latency, known limitations, rollback reference.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/changelog --release v5
/changelog --audience users          → user-facing version without model internals
```

**What you get:** `outputs/reports/changelog-[system]-v[n].md`: internal entry (versions, tuple, deltas, manifests) and, on request, a user-facing entry in plain language.

**Time:** 10 minutes.

---

# /changelog

## Internal entry

```
## v5 — 2026-09-04
Change: system prompt v4 → v5 (added decline path + 2 benign medical-adjacent examples). Model unchanged (sonnet-4-5@2025-09-29).
Evals (golden refusal-v3, n=412, paired): refusal precision 0.81 → 0.91 [+0.06, +0.14]; task accuracy 0.874 → 0.869 [−0.02, +0.01] (no evidence of change); over-refusal FM-004 rate 5.1% → 1.2%.
Cost/1k $3.10 → $3.42. p95 2,810 → 2,980 ms.
Known: FM-009 (medical-adjacent over-refusal) mitigated, not closed. Manifest: outputs/experiments/2026-09-03-v5. Rollback: prompt v4 via flag `summariser_prompt_version`.
```

## User-facing entry

Plain language, benefit first, honest about limits. `{ai-eng-os}/voice/writing-style-exec.md` register at 8th-grade reading level.

## Rules

- Deltas with CIs internally; no CIs in the user-facing text, but no overclaiming either.
- Every entry links a manifest and names the rollback.
