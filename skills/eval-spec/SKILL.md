---
name: eval-spec
description: Write the eval before the change. Defines what's measured, the dataset, the grader, sample size, baseline and pass/fail thresholds. The entry point for every prompt, model, data or scaffold change.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/eval-spec                                  → guided; I ask what you're about to change
/eval-spec "refusal behavior on the support bot"
/eval-spec --type safety --gated            → safety eval that will gate releases
/eval-spec --from-traces outputs/traces/    → derive the task definition and slices from real traces
```

**What you get:** `outputs/evals/[name]-spec-v1.md` from `{ai-eng-os}/templates/eval-spec-template.md`, with dataset plan, grader choice, n, thresholds and a baseline table to fill. Then `/eval-build` turns it into a runnable harness.

**Time:** 15–30 minutes.

---

# /eval-spec - Spec the eval first

Nothing ships without a number, and the number needs a definition. This skill produces that definition.

## Context routing

| Source | Look for | Use |
|---|---|---|
| `context-library/project-brief.md` | gated metrics, budgets, task types | anchor the eval to what's already gated |
| `context-library/evals/` | existing golden sets, past specs | extend rather than duplicate |
| `context-library/failure-modes.md` | open failure modes | every open FM gets items in the set |
| `context-library/prompts/` | behavior contract of the prompt under test | one behavior line → one eval slice |
| `{ai-eng-os}/frameworks/eval-taxonomy.md` | eval kind, grading level, sizing | pick the cheapest valid grader |
| `{ai-eng-os}/frameworks/eval-validity-checklist.md` | threats | pre-empt them in the spec |

Cross-skill: sizing → `/stats-power`; judge → `/judge-calibrate`; dataset → `/golden-set-curate`; if the metric should tie to a business outcome and PM OS is installed → `/pm-os:impact-sizing`.

## Step 1: Clarify (skip what's already answered)

```
Before I write the spec:
1. What are you about to change? (prompt / model / data / retrieval / tool / scaffold)
2. What should get better, in a sentence a user would recognise?
3. What must not get worse? (I'll pull gated metrics from project-brief.md)
4. Do you have real inputs I can sample (traces, logs, tickets)? Roughly how many?
5. Will this eval gate releases, or is it for iteration only?
```

Follow-ups when needed: "Is there a checkable form for the answer (exact value, schema, test), or is it open text?" · "Which slices matter: language, segment, difficulty, input length?" · "Any items the model may have seen in training?"

## Step 2: Choose the design

Decide and justify, in this order:
1. **Kind**: capability / behavior / safety / regression. Most changes need a capability or behavior eval plus the existing regression suite.
2. **Grader**: cheapest level that's valid (code → reference → LLM judge → pairwise → human). If LLM judge, name the rubric from `{ai-eng-os}/rubrics/` and schedule `/judge-calibrate`.
3. **Metric(s)**: primary, guardrails, plus cost per 1k and p95 always.
4. **n**: from the effect size you'd act on. Quote the rule of thumb and recommend `/stats-power` for the real number.
5. **Splits**: golden (frozen, gated) vs dev. Contamination check method.
6. **Thresholds**: ship if / stop if, in numbers.

## Step 3: Write the spec

Fill `{ai-eng-os}/templates/eval-spec-template.md`. Save to `outputs/evals/[name]-spec-v1.md`. Include an "items to write" table: slice × count × example, so `/golden-set-curate` has a target.

## Step 4: Hand off

```
Spec saved to outputs/evals/[name]-spec-v1.md.

Next:
- /golden-set-curate to build the items (target n = [ ])
- /eval-build to generate the harness
- /baseline to get the first number before you change anything
```

## Rules

- Refuse to skip the baseline. If the user wants to change the prompt today, the spec can be short, but the baseline runs first.
- Never propose iterating against the golden set.
- If an LLM judge is chosen, the spec is incomplete until calibration is planned.
- Always include at least one slice where you expect the change to hurt.
