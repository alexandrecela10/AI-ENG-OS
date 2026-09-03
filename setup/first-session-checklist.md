# First Session Checklist

Verify AI Engineering OS works end to end in a real project repo.

## Overview

By the end you'll have:
- Confirmed the plugin loads (Devin or Claude Code)
- Scaffolded the per-repo workspace with `/ai-init`
- Filled the project brief and stakeholders
- Imported your existing evals, prompts and datasets
- Written an eval spec, run a baseline, iterated a prompt once
- Run a reviewer persona and a full experiment writeup
- A verification checklist you can hand to the next engineer

**Time needed:** 40–60 minutes (longer if you wire the harness to a real model).

Commands below are shown as `/skill`. In Devin Cloud they're `/ai-eng-os:skill`; in Claude Code you type the same `/skill`.

---

## Pre-Flight Check

```bash
# 1. You're in your PROJECT repo, not the plugin
pwd
git rev-parse --show-toplevel

# 2. Plugin is installed
devin plugins list | grep ai-eng-os        # CLI / Desktop
# or: check the marketplace manifest in Devin Cloud
# or: ls ../ai-eng-os/CLAUDE.md             # Claude Code side-by-side

# 3. (Optional, only for running evals) a model key is set
test -n "$ANTHROPIC_API_KEY" && echo set || echo missing

# 4. Python 3.10+ for the scaffolds
python3 --version
```

All good? Continue.

---

## Setup Step 1: Scaffold the workspace

**What we're doing:** creating the empty per-repo folders every skill reads from and writes to.

```
/ai-init --dry-run
```

**Expected result:** a tree of what would be created. Nothing written.

```
/ai-init --domains ml,causal,stats
```

**Expected result:**
- `context-library/` with 8 subfolders, each containing `.gitkeep`
- `context-library/project-brief.md`, `stakeholders.md`, `failure-modes.md`, `README.md`
- `outputs/` with 15 subfolders plus `ml/ causal/ stats/`
- A "Created / Skipped" report

```bash
git status --short | head -30
git add context-library outputs && git commit -m "Add AI Engineering OS workspace"
```

Run `/ai-init` a second time. **Expected:** everything listed under "Skipped (already present)", nothing overwritten.

✅ **Mark complete when:** the folders exist, are committed, and a second run changes nothing.

---

## Setup Step 2: Fill the project brief

**What we're doing:** giving every skill the context it checks first.

```
Help me fill context-library/project-brief.md. The system is [what it does] for [users].
Model stack: [provider/model]. Gated metrics today: [e.g. task pass rate, refusal precision].
Budgets: [$/1k requests, p95 ms]. Known failure modes: [list]. Safety lines: [what it must never do].
```

**Expected result:** the brief is filled with your numbers, and Claude/Devin asks about anything missing (budgets and gated metrics are the usual gaps). Then:

```
Help me fill context-library/stakeholders.md: tech lead is [name], product is [name],
safety approver is [name], on-call is [rotation].
```

✅ **Mark complete when:** `project-brief.md` has at least one gated metric with a target, a cost budget, a latency budget, and `stakeholders.md` names a launch approver.

---

## Setup Step 3: Import existing work

**What we're doing:** moving what you already have into `context-library/` so skills stop asking.

```
I have existing material to organise into context-library/. Read each and tell me where it goes:
- eval sets / golden sets            → context-library/evals/
- current production prompts         → context-library/prompts/
- dataset notes / cards              → context-library/datasets/
- past experiment writeups           → context-library/experiments/
- ADRs / decision docs               → context-library/decisions/
- postmortems                        → context-library/incidents/
- design docs                        → context-library/design-docs/
- anything else                      → context-library/other/
Don't rewrite them; just place them and list what's missing a version or a hash.
```

**Most useful to import first:** the current production prompt(s), any eval set you trust, the last incident.

If you have nothing yet, skip this step. The first experiment will create the seeds.

✅ **Mark complete when:** your current prompt and any eval set you have are in `context-library/`, and any eval set has a recorded sha256 (`shasum -a 256 <file>`).

---

## Test 1: File reading

**What we're testing:** the assistant reads the working repo's context, not the plugin's.

```
What are the gated metrics and budgets for this project, and who approves a launch?
```

**Expected result:** answers quoting `context-library/project-brief.md` and `stakeholders.md`. If it says it can't find them, you're in the wrong directory or `/ai-init` ran elsewhere.

✅ **Mark complete when:** it quotes your numbers and names.

---

## Test 2: Skill invocation and the two-root rule

```
/problem-framing "make the [feature] answers better"
```

**Expected result:**
- Clarifying questions (user, task type, what "better" means, cost of errors)
- A file at `outputs/design-docs/[slug]-framing.md`
- A recommendation to run `/eval-spec` next
- Nothing written anywhere except `outputs/`

```bash
git status --short          # only outputs/ should change
```

✅ **Mark complete when:** the file exists under `outputs/` and nothing changed in `context-library/` or the plugin.

---

## Test 3: Eval spec

**What we're testing:** the center of the OS.

```
/eval-spec "[the thing you're about to change, e.g. the summariser system prompt]"
```

**Expected result:** `outputs/evals/[slug]-spec-v1.md` with task, dataset (golden vs dev), grader choice, metrics, sample size with a detectable-effect estimate, baseline requirement, and thresholds. If you have fewer than ~200 items it should say so and suggest `/stats-power` or `/golden-set-curate`.

Try the stats pack on it:

```
/stats-power outputs/evals/[slug]-spec-v1.md
```

**Expected result:** required n or detectable effect at your n, with a sensitivity table.

✅ **Mark complete when:** the spec names a grader, a golden set (or a plan to build one), and a pass threshold.

---

## Test 4: Build the harness and run a baseline

```
/eval-build outputs/evals/[slug]-spec-v1.md
```

**Expected result:** `outputs/scaffolds/eval-harness/` copied from the plugin and adapted: your dataset path, your grader, and a `call_model()` that points at your project's model client (or a clear TODO if none exists).

Smoke test without a model key (uses the exact-match grader and a stub):

```bash
cd outputs/scaffolds/eval-harness
python3 -c "import harness, stats; print(stats.wilson(83, 100))"
```

**Expected result:** a tuple like `(0.744, 0.895)`.

With a key, run the baseline:

```
/baseline outputs/evals/[slug]-spec-v1.md
```

**Expected result:** `outputs/experiments/<date>-baseline-<slug>/` with `manifest.json`, `results.jsonl`, `summary.json` and a report showing the trivial, current and raw-model rows with CIs, cost/1k and p95.

✅ **Mark complete when:** a manifest exists with a dataset sha256, model snapshot, and metrics with CIs.

---

## Test 5: One prompt iteration

```
/prompt-spec context-library/prompts/[current prompt]
```

**Expected result:** a behavior contract in `outputs/prompts/`, and the prompt registered with version + hash.

```
/prompt-iterate prompts/[name]@v1 --against outputs/experiments/<baseline id>/
```

**Expected result:**
- Loss clusters from the baseline results
- A hypothesis with a predicted delta
- One change (it should refuse to make two)
- A run on dev with a paired delta and CI, cost and p95
- A verdict: evidence / no evidence / regression
- A new manifest folder

Ask it to make two changes at once. **Expected:** it declines and explains the one-variable rule.

✅ **Mark complete when:** you have two manifests (baseline and iteration) and a paired delta with a CI.

---

## Test 6: Reviewer persona

```
/eval-review outputs/experiments/<iteration id>/
```

**Expected result:** the eval-skeptic walks the validity checklist, gives a verdict (evidence / weak / not yet), and names the smallest follow-up run.

Try the fast version on a claim:

```
/skeptic "v2 is better, ship it"
```

**Expected result:** three ways it's wrong ranked, the cheapest check, the softened claim. Short.

✅ **Mark complete when:** the review cites your actual n and CI, not generic advice.

---

## Test 7: Domain packs (optional)

Pick one:

```
/ml-problem-framing "predict [something] from [features]"
/causal-question "did [change] cause [outcome]?"
/stats-result-check "accuracy went from 0.84 to 0.88 on 50 examples"
```

**Expected result:** output in `outputs/ml/`, `outputs/causal/` or inline; the stats check should say that n = 50 can't support the claim and give the honest CI.

✅ **Mark complete when:** at least one pack skill produced its expected artefact.

---

## Test 8: End-to-end writeup

```
/experiment-writeup outputs/experiments/<iteration id>/
```

**Expected result:** `writeup.md` with TL;DR, predicted vs actual, setup, results table with CIs, where it hurt (trace links), threats to validity, decision, and an offer to log the calibration line to `context-library/ai-eng-os-learning-log.md`.

Accept the offer. **Expected:** it proposes the diff and waits for approval before writing to `context-library/`.

✅ **Mark complete when:** the writeup passes `rubrics/writeup-standard.md` (ask: "check this against the writeup standard").

---

## Error Recovery

| Symptom | Likely cause | Fix |
|---|---|---|
| "Can't find project-brief.md" | wrong directory, or `/ai-init` ran in the plugin | `cd` to the project root; re-run `/ai-init` |
| Skill not found | plugin not installed / not in marketplace manifest | `devin plugins list`; check settings; restart the session |
| Files appearing in the plugin repo | two-root confusion | tell it: "Working repo is `<path>`, plugin root is read-only"; move the files |
| `NotImplementedError` from `call_model` | harness not wired to your client | edit `harness.py::call_model` to call your project's model client |
| CI on dev and golden mixed | spec didn't separate sets | `/golden-set-curate --freeze`; record the hash in the spec |
| Delta reported without CI | old harness copy | re-copy `stats.py`, use `paired_delta_ci` |
| Judge scores look random | judge not calibrated | `/judge-calibrate` before trusting |

---

## Verification Checklist

- [ ] `/ai-init` idempotent; workspace committed
- [ ] Project brief has gated metrics and budgets; stakeholders has a launch approver
- [ ] Existing prompt and eval set imported with hashes
- [ ] Skills write only to `outputs/`
- [ ] Eval spec exists with grader, golden set and threshold
- [ ] Baseline manifest with dataset sha256, model snapshot, CIs, cost, latency
- [ ] One iteration with a paired delta and CI
- [ ] Two-change request refused
- [ ] `/eval-review` verdict cites your numbers
- [ ] Writeup meets the standard; calibration line proposed, not silently written

---

## Next Steps

- `/prompt-regression --setup-ci` so the golden set gates every PR.
- `/red-team` on the current prompt; add findings to the regression suite.
- `/cost-latency-budget` to see where tokens go.
- Friday: `/weekly-review` then `/status-update`.
- If PM OS is installed, hand `/pm-os:impact-sizing` results into `/eval-spec`.
