---
name: finetune-plan
description: Decide whether to fine-tune and plan it if so: the prompt-engineering ceiling check, data requirements, method (SFT / preference / distillation), eval plan, cost, and the serving implications.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/finetune-plan "classification of support tickets into 40 categories"
/finetune-plan --distill --teacher claude-sonnet-4-5 --student <small model>
```

**What you get:** `outputs/design-docs/finetune-[slug].md`: the go/no-go with reasons, data plan (size, source, card), method, hyperparameter search budget, eval plan with the prompt-engineered baseline as the bar, cost estimate, serving and monitoring changes, and the ML-pack skills to run next.

**Time:** 45 minutes.

---

# /finetune-plan

Fine-tuning is a commitment: a training pipeline, a data pipeline, a serving change and a new drift surface. Earn it.

## Step 1: The ceiling check

Before planning, confirm:
- Prompt engineering has been pushed (`/prompt-iterate` history shows two consecutive no-evidence iterations, or the token budget is the blocker).
- Retrieval is not the bottleneck (`/rag-design --debug`).
- A cheaper model with the good prompt doesn't already meet the bar (`/baseline` cheap-model row).

If any of these is unchecked, say so and stop.

## Step 2: Plan

1. **Goal**: match/beat the prompt-engineered big model on [metric] at [x]× lower cost/latency, or exceed it on a narrow task.
2. **Method**: SFT on labelled pairs; distillation from a teacher's outputs (filtered by a verifier); preference tuning when "better" is a judgement. Pick one; say why not the others.
3. **Data**: n needed (start small: hundreds to low thousands for narrow tasks), sources, card, leakage check vs golden (`/ml-data-split-audit`).
4. **Eval**: same golden set as the prompt baseline, plus a held-out slice for generalisation; regression and safety suites still apply.
5. **Training**: budget for hyperparameter search, equal across compared configs; seeds; checkpoints; `/ml-training-plan`.
6. **Serving**: where it runs, latency/cost projection, rollback to the prompt baseline.
7. **Monitoring**: drift on inputs and outputs (`/ml-monitoring-plan`).

## Rules

- The bar is the prompt-engineered baseline, not zero-shot.
- Golden set untouched by training data, verified by hash.
- Safety evals re-run; fine-tuning can erode refusal behavior.
