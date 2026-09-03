---
name: prompt-regression
description: Run the regression suite (golden + failure-mode cases) against a release candidate and produce a pass/fail gate with the delta table. Sets up the pre-push hook and CI job when asked.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/prompt-regression                              → run every registered prompt's gated evals against its floors
/prompt-regression prompts/summariser.md@v5     → one prompt
/prompt-regression --setup-hook                 → add pre-push hook running the changed prompts' suites
/prompt-regression --setup-ci                   → propose a GitHub Actions job that posts the delta table as a PR comment
```

**What you get:** `outputs/evals/regression-[date].md`: per prompt, per gated metric: value, floor, CI, pass/fail; list of newly failing item ids with their FM tags; overall gate result. Optional hook/CI files in `outputs/scaffolds/`.

**Time:** minutes to run; 20 minutes to set up hook + CI.

---

# /prompt-regression

Regression is the eval kind that only grows. Every closed failure mode has a case here forever.

## Steps

1. **Collect** registered prompts (`prompt-registry/registry.py:all_prompts()`), each with `eval`, `grader`, `gated_metrics`.
2. **Run** each against its eval at temperature 0 with the pinned snapshot. Use the harness.
3. **Gate.** Metric below floor → FAIL. Metric inside CI of floor → WARN (say so; don't call it a pass).
4. **Diff** newly failing items vs the last green run; group by FM tag; link traces.
5. **Report** and, if FAIL, refuse to call the candidate releasable. Offer `/trace-debug` on the failing cluster.

## Hook (`--setup-hook`)

Writes `outputs/scaffolds/hooks/pre-push` that runs `test_prompts.py --changed-only`. The engineer installs it (`ln -s` into `.git/hooks/` or via the repo's hook manager). Never install into `.git/` without being asked.

## CI (`--setup-ci`)

Proposes `outputs/scaffolds/ci/eval-regression.yml`: on PR touching `prompts/**`, `evals/**` or model config, run the suite and post the delta table as a PR comment; fail the check if any gated metric is below floor. Secrets via the repo's existing secret store; never in the file.

## Rules

- Floors come from the prompt frontmatter and eval spec, not from the run.
- A WARN is not a PASS.
- Regression cases are never deleted, only superseded with a note.
