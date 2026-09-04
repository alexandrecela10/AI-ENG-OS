# Eval Harness Guide

How to go from `{ai-eng-os}/scaffolds/eval-harness/` to an eval you can trust.

## 1. Copy, don't import

`/eval-build` copies the scaffold into `outputs/scaffolds/eval-harness/` (later moved to `src/evals/` or wherever your project keeps tests). The project owns the copy. Upgrades to the plugin never overwrite it; cherry-pick what you want.

## 2. Wire the model

`harness.call_model(system, user, model) -> (text, usage)` raises `NotImplementedError` on purpose. Replace the body with a call through your project's existing client so retries, auth, logging and cost accounting match production. Return `usage` as a dict with at least `input_tokens`, `output_tokens`, and `usd` if you can compute it; the manifest writer reads those.

Pin the snapshot in the CLI flag (`--model claude-sonnet-4-5@2025-09-29`), not in code.

## 3. Dataset schema

One JSON object per line:

```json
{"id": "ref-0412", "input": {"question": "...", "context": "..."}, "expected": "...", "tags": ["fr", "long", "FM-004"], "source": "prod-trace:2026-08-14", "split": "golden"}
```

- `id` stable forever (regression cases reference it).
- `tags` drive slice tables; include the language, length bucket and any failure-mode id.
- `split` is `golden` or `dev`. Never mix in one file.
- Record the sha256 of the file in the eval spec and every manifest. `harness.sha256(path)` does it.

## 4. Choose the grader

| Situation | Grader | Notes |
|---|---|---|
| single correct answer, short | `ExactMatch` | normalises whitespace/case; accepts a list of alternatives in `expected` |
| structured output | `JsonSchemaGrader` | required keys and types; extend for enums/ranges |
| checkable property (cites a source, under N words, calls no gated tool) | write a small code grader implementing `Grader` | cheapest and most reliable; prefer whenever possible |
| quality judgement (faithfulness, helpfulness) | `LlmJudge` with a rubric from `{ai-eng-os}/rubrics/` | judge model fixed, temperature 0, calibrated first |
| "which is better" | pairwise rubric | swap positions, report consistency |

Graders return `GradeResult(score, passed, scale, reason, details)`. Keep `reason` short and human-readable; it shows up in the loss table.

## 5. Calibrate the judge before you trust it

`/judge-calibrate`: 100–200 items with human labels (two labellers, report agreement), judge-human kappa, position bias (swap A/B), length bias (correlation of score with length), self-preference (judge scoring its own family), self-consistency (3 repeats). Choose the pass threshold that best matches humans. Record the judge model, rubric hash and threshold in the manifest under `grader`.

Rule of thumb: kappa < 0.6 → don't gate on this judge; use it for triage only.

## 6. Statistics

`stats.py`:
- `wilson(successes, n)` for a single pass rate.
- `bootstrap_mean_ci(values)` for continuous scores (latency, judge scores).
- `paired_delta_ci(a, b)` for comparing two runs on the same items. **Always paired** when the items are the same; unpaired CIs are roughly 2× too wide and you'll miss real improvements or, worse, declare noise as signal when you eyeball two bars.

Report `Δ [lo, hi]` on every comparison. If the CI includes 0: "no evidence of a change". Verdict language lives in `{ai-eng-os}/domains/stats/frameworks/uncertainty-reporting.md`.

## 7. Outputs and the manifest

Every run writes to `outputs/experiments/<date>-<slug>/`:
- `results.jsonl`: one row per item (id, output, grade, tokens, latency_ms, trace_id).
- `summary.json`: metrics with CIs, per-slice, cost/1k, p50/p95.
- `manifest.json`: the versioned tuple. Template: `{ai-eng-os}/templates/experiment-manifest.json`. Fill `baseline.run_id` and `delta_vs_baseline` when comparing.

Never edit `results.jsonl` by hand. Re-run.

## 8. Golden vs dev

- **Dev**: iterate freely. Look at losses. Change things.
- **Golden**: frozen (hash), touched only to confirm a candidate you'd ship. Every look is logged in the manifest (`golden_touches`).
- Refresh golden quarterly or after a distribution shift; version it (`refusal-v3.jsonl`), never edit in place.

Contamination check before promoting: id and content-hash overlap between golden and anything used to tune (few-shot examples, fine-tuning data, dev). `/golden-set-curate` runs it.

## 9. Non-determinism

Temperature 0 for anything graded or parsed. If you must evaluate at temperature > 0, run 3–5 repeats and report the between-run sd; a single run is one sample.

## 10. Cost and latency in every table

The harness records tokens and wall time per item. `summary.json` reports cost/1k and p50/p95. When comparing models, add cost per correct answer. A 2-pt accuracy gain at 3× cost is a decision, not a win.

## 11. CI

`/prompt-regression --setup-ci` adds a workflow that runs the regression suite (golden + failure-mode cases) on PRs touching prompts, graders or model config, and posts the delta table as a comment. Floors come from the eval spec. Keep the CI suite under ~10 minutes; the full golden run can be nightly.

## 12. When the harness lies

Symptoms and causes: pass rate jumps 10+ pts from a small prompt tweak (contamination or grader bug); judge agrees with itself but not humans (rubric drift); results differ between two "identical" runs (temperature, snapshot drift, non-deterministic tool). Run `/eval-review` and walk `{ai-eng-os}/frameworks/eval-validity-checklist.md`.
