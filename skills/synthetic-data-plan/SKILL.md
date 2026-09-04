---
name: synthetic-data-plan
description: Plan model-generated data for evals or training: what to generate, with which generator and prompt, how to enforce diversity, how to verify with a different model, and how to avoid evaluating on your own generator's distribution.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/synthetic-data-plan "adversarial prompts for the refusal eval, 200 items"
/synthetic-data-plan --for training --seed-data data/real-200.jsonl
```

**What you get:** `outputs/datasets/synthetic-plan-[slug].md`: purpose, generator (model + versioned prompt), seed strategy, diversity controls, verifier design, filtering thresholds, contamination guard, expected yield, and the generation prompt itself in `outputs/prompts/gen-[slug].md`.

**Time:** 30 minutes.

---

# /synthetic-data-plan

Synthetic data is cheap to make and expensive to trust. Plan the trust part first.

## Steps

1. **Purpose and shape.** Eval or training? Which slices are thin? Target counts per slice.
2. **Generator.** Model + pinned snapshot; a versioned generation prompt with 3–5 real seeds per slice (`--seed-data`); temperature > 0 with n repeats; persona/scenario grids for diversity.
3. **Diversity controls.** Distinct n-gram ratio target; embedding-spread check; per-template caps; reject near-dups (pipeline scaffold).
4. **Verifier.** A different model family (or humans on a sample) checks each item against a rubric: valid, on-slice, not trivially solvable, no PII. Report acceptance rate.
5. **Contamination guard.** Mark `source: synthetic:<generator>` in every item. Never eval a system on synthetic items from its own model family without flagging it in the spec.
6. **Yield estimate.** Generate → verify → dedupe; expect 30–60% survival. Budget accordingly.
7. **Card.** Every synthetic set gets `/dataset-card` with the generator prompt hash.

## Rules

- Real seeds in, or the distribution will be the model's imagination.
- Verifier ≠ generator.
- Synthetic items in golden sets are labelled as such and capped (suggest ≤ 30%).
