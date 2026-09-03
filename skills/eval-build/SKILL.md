---
name: eval-build
description: Turn an eval spec into a runnable harness by copying and adapting {ai-eng-os}/scaffolds/eval-harness (dataset schema, grader, CIs, manifest writer) into the working repo.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/eval-build outputs/evals/refusal-spec-v1.md      → harness + grader + empty dataset file for that spec
/eval-build --grader llm_judge --rubric faithfulness
/eval-build --platform langfuse                    → wire results to an existing tracing/eval platform instead of local files
```

**What you get:** `outputs/scaffolds/eval-harness/` adapted to the spec (grader chosen, dataset schema with the spec's slices, rubric copied, `call_model()` stub pointing at the project's client), plus `evals/golden/[name]-v1.jsonl` with 3 example items in the right shape. You move it into `src/` or `evals/` when happy.

**Time:** 10 minutes, then wiring the model client.

---

# /eval-build - From spec to runnable harness

## Context routing

| Source | Use |
|---|---|
| the eval spec (argument) | grader, metrics, slices, n |
| `context-library/project-brief.md` | model, provider, tracing platform |
| existing repo code | reuse the project's model client, don't add a second one |
| `{ai-eng-os}/scaffolds/eval-harness/` | source to copy |
| `{ai-eng-os}/rubrics/` | judge prompts |

## Steps

1. **Read the spec.** Extract: grader type, metrics, slices, gated thresholds, dataset path.
2. **Copy the scaffold** to `outputs/scaffolds/eval-harness/`. Never edit `{ai-eng-os}` in place.
3. **Adapt**:
   - Pick the grader in `harness.py`; delete the ones not needed.
   - If `llm_judge`: copy the rubric to `rubrics/`, set the judge model (a different family from the system under test, or note the self-preference risk), temperature 0.
   - Put the spec's slices into `schema.md` and the example items.
   - Set `PRICE_PER_1K_TOKENS` for the model in the brief.
   - Point `call_model()` at the project's existing client. If none exists, leave the stub and say so.
4. **Write 3 example items** in `evals/golden/[name]-v1.jsonl`: one happy path, one edge case, one from an open failure mode.
5. **Add the run command** to the spec's "Baseline" section and to a `README` in the harness folder.
6. **If CI exists**, propose a job that runs the regression subset on PRs and posts the summary as a comment (`{ai-eng-os}/rubrics/code-review-standard.md` § Evals in CI).

## Report

```
Harness ready at outputs/scaffolds/eval-harness/ (grader: llm_judge, rubric: faithfulness-v1).
call_model() is wired to src/llm/client.py:complete().
3 example items in evals/golden/refusal-v1.jsonl. Target n from spec: 400.

Next: /golden-set-curate to fill the dataset, then /baseline.
```

## Rules

- Temperature 0 and a pinned snapshot in the default config.
- Never hardcode API keys; read from the project's existing config or env.
- Keep the harness dependency-light. Use what the repo already has.
- The manifest writer stays. Every run produces `manifest.json`.
