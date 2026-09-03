---
name: ml-problem-framing
description: Frame a prediction problem: target, decision it drives, metric chosen from the decision, cost of errors, unit of split, and whether ML beats a rule. ML pack.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/ml-problem-framing "predict which trials convert to paid"
/ml-problem-framing --from outputs/design-docs/churn-framing.md
```

**What you get:** `outputs/ml/[slug]-framing.md`: target definition (with timing), decision and threshold, metric with justification, cost matrix, split unit, trivial baseline to run, data needed, go/no-go on ML vs a rule.

**Time:** 30 minutes.

---

# /ml-problem-framing

Reference: `{ai-eng-os}/domains/ml/frameworks/ml-lifecycle.md`, `{ai-eng-os}/domains/ml/frameworks/metric-selection.md`.

## Clarify

```
1. What decision will the prediction drive, and who acts on it?
2. Target: exactly what, measured when? (define the prediction time and the label window)
3. What does a false positive cost? A false negative?
4. Will the model see the future at deployment? (→ time split)
5. Is there a rule or heuristic that does this today? How well?
6. How much labelled data, over what period?
```

## Write

Target and timing · decision + threshold · metric (from the table) + guardrails · cost matrix · split unit · trivial baseline · data inventory · ML vs rule verdict · first experiment → `/ml-data-split-audit` then `/ml-baseline`.

## Rules

- No metric without the decision it serves.
- If a rule gets 80% of the value, say so.
- Feature importance is not causation; route "why" questions to `/causal-question`.
