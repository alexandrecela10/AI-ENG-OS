---
name: skeptic
description: Fast devil's advocate on any claim, plan or result. Names the most likely way it's wrong, the cheapest test of that, and how much to soften the claim meanwhile.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/skeptic "v5 is ready to ship"
/skeptic outputs/experiments/2026-09-03-v5/writeup.md
/skeptic --causal "the new prompt reduced churn"            → uses causal-skeptic instead
```

**What you get:** inline (or `outputs/reports/skeptic-[slug].md` on request): three ways it's probably wrong, ranked; the cheapest check for the top one; the softened claim you can defend today.

**Time:** 5 minutes.

---

# /skeptic

Default persona: `{ai-eng-os}/agents/eval-skeptic.md`. `--causal` → `causal-skeptic.md`. `--stats` → `statistician.md`. `--ops` → `ops-reviewer.md`.

## Method

1. Restate the claim precisely, with the number and population it applies to.
2. List the three most likely alternative explanations or failure points, ranked by probability × damage.
3. For the top one, the cheapest observation that would rule it in or out.
4. The claim as it can honestly be stated right now.

## Rules

- Specific over general: "n=42 on fr gives ±15 pts" not "sample may be small".
- Short. This is a gut check, not a review; `/ai-review-panel` is the full version.
- Never hostile. The point is to ship things that are true.
