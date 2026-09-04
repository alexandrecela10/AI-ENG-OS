---
name: ai-review-panel
description: Multi-persona review of any artefact (design doc, eval spec, writeup, launch readiness, model card) using the reviewer personas in {ai-eng-os}/agents/. Synthesises findings, flags conflicts, ranks blockers.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/ai-review-panel outputs/design-docs/triage-agent-design.md
/ai-review-panel outputs/experiments/2026-09-03-v5/writeup.md --personas eval-skeptic,statistician,research-scientist
/ai-review-panel --all                                     → all ten personas (long)
```

**What you get:** `[artefact path]-review.md` next to the artefact in `outputs/`: per-persona findings (blocking / non-blocking), a synthesis, conflicts between personas with a recommendation, and a ranked action list.

**Time:** 15–30 minutes.

---

# /ai-review-panel

## Default panels by artefact

| Artefact | Personas |
|---|---|
| framing / design doc | infra-reviewer, safety-reviewer, eval-skeptic, user-advocate |
| eval spec / run / writeup | eval-skeptic, statistician, research-scientist |
| agent design / tool schemas | infra-reviewer, red-teamer, safety-reviewer |
| launch readiness / rollout | infra-reviewer, safety-reviewer, ops-reviewer, user-advocate |
| ML work | ml-reviewer, statistician, eval-skeptic |
| causal analysis | causal-skeptic, statistician, research-scientist |
| stats analysis | statistician, research-scientist |

## Method

1. For each persona, read its file in `{ai-eng-os}/agents/`, adopt it fully, review the artefact, output findings tagged blocking / non-blocking with a one-line fix each.
2. Synthesise: what everyone agrees on; where they conflict (e.g. infra wants a smaller model, eval-skeptic says the accuracy delta isn't proven) and a recommendation.
3. Rank actions by blocker-ness × effort.
4. Save. Offer to apply the low-effort fixes to the artefact (re-read the file, apply only those, never regenerate).

## Rules

- Personas stay in character; no averaging into mush.
- Blocking means "would stop a launch or invalidate a result", nothing less.
- In Devin Cloud, personas run inline (subagents are CLI/Desktop only today); the output is the same.
