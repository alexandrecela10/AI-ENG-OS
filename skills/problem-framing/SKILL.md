---
name: problem-framing
description: Turn a vague ask ("make the bot better", "add AI to X") into a framed engineering problem with a user, a task type, a measurable outcome, constraints, and a decision on whether a model is even the right tool.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/problem-framing "summarise support tickets for account managers"
/problem-framing --from-prd outputs/prds/ticket-summary.md     → from a PM OS PRD
/problem-framing --no-model-check                              → skip the "do you need a model" step
```

**What you get:** `outputs/design-docs/[slug]-framing.md`: problem statement, user and task type, success metric with a target, constraints, the model/no-model decision, the first eval to spec and the first baseline to run.

**Time:** 20–40 minutes.

---

# /problem-framing

Most wasted AI engineering time comes from building before framing. This skill costs half an hour and saves weeks.

## Context routing

| Source | Use |
|---|---|
| `context-library/project-brief.md` | existing metrics, budgets, constraints |
| `context-library/design-docs/`, `decisions/` | don't re-decide settled things |
| `outputs/prds/` (PM OS) | user problem, impact sizing |
| `context-library/failure-modes.md` | what's already known to go wrong |

## Step 1: Clarify

```
1. Who has the problem, and what do they do today without this?
2. What does "better" look like to them, in an observable way?
3. What's the task type? (classify / extract / generate / summarise / route / answer-from-docs / plan-and-act)
4. What happens when the system is wrong? Who catches it?
5. Hard constraints: cost per use, latency, data that can't leave, policy lines.
6. Is there a non-model way to do 80% of this? (rules, search, a form, a human)
```

## Step 2: The model/no-model check

Score honestly:
- Inputs are unstructured natural language or images → model helps.
- Output must be exactly right every time with no human check → model is risky; consider model-assisted human, or rules.
- Task has a checkable answer (tests, schema, lookup) → great, the eval is cheap.
- Volume is low and each case is high stakes → a human with a good tool may beat a model.

Write the verdict: **model / model-assisted / no model**, with the reason.

## Step 3: Frame

```
Problem: [who] needs [outcome] because [why]; today [current state, with a number].
Task type: [ ]. Input: [ ]. Output: [ ].
Success metric: [metric] from [current] to [target] on [population] by [when]. Guardrails: [cost], [latency], [safety metric].
Constraints: [ ].
Failure cost: [what a wrong output does; who catches it].
Decision: model / model-assisted / no model.
First eval: [kind, grader, rough n] → /eval-spec
First baseline: [simplest thing: a rule, a retrieval-only answer, the current process] → /baseline
Open questions: [ ] — @owner
```

Save to `outputs/design-docs/[slug]-framing.md`.

## Hand off

`/eval-spec` for the eval, `/baseline` for the number, `/design-doc` when the approach is chosen. If PM OS is installed and the impact isn't sized, `/pm-os:impact-sizing`.

## Rules

- No architecture in the framing doc. That's the design doc's job.
- The success metric must be observable without the model (so you can baseline it).
- Say plainly when the honest answer is "don't use a model here".
