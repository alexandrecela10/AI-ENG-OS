---
name: trace-debug
description: Debug model or agent behavior from traces. Clusters failures, maps them to failure-mode categories, finds the step where things went wrong, and proposes one fix plus the regression cases to add.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/trace-debug outputs/experiments/2026-09-03-v4/results.jsonl --failed
/trace-debug outputs/traces/2026-09-02/ --sample 50
/trace-debug --trace lf-8a91c2                              → one trace, deep dive
```

**What you get:** `outputs/reports/trace-debug-[date].md`: failure clusters (count, share, FM category, example ids), the step or component at fault per cluster, one proposed fix per cluster ranked by expected impact, and proposed additions to `failure-modes.md` and the golden set (as a diff for approval).

**Time:** 30–60 minutes.

---

# /trace-debug

Numbers say whether; traces say why.

## Method

1. **Collect** failed items or a random sample of traces. Read at least 20 in full before clustering.
2. **Cluster** by observable symptom, then map each to `{ai-eng-os}/frameworks/failure-mode-catalogue.md` categories and existing FM ids.
3. **Locate** the fault per cluster: input (bad/adversarial), retrieval (missing/stale), prompt (missing rule/example), model (capability), tool (bad result/schema), loop (budget/repeat), parsing. For agents, name the step number where the trajectory diverged.
4. **Hypothesise** one fix per cluster with predicted effect. Prefer the fix that addresses the largest cluster with the smallest change.
5. **Regression.** For each new FM, draft 5 golden items tagged with the id.
6. **Offer** (never silently apply) the `failure-modes.md` rows and golden items.

## Report

```
Clusters (n=87 failures of 412):
1. 41 (47%) fabricated citation → FM-001. Fault: retrieval returned 0 docs; prompt has no decline path. Fix: add decline rule + example. Predicted: −35 failures.
2. 22 (25%) over-refusal on medical-adjacent benign → new FM-009. Fault: prompt rule "never give medical advice" too broad. Fix: narrow rule + 2 benign examples.
3. 14 (16%) format: trailing prose after JSON → FM-005 (known). Fault: no stop sequence. Fix: parser tolerance + stop seq.
4. 10 (11%) misc, no pattern → keep watching.
Next experiment: fix 1 via /prompt-iterate. Regression items drafted: 10.
```

## Rules

- Read traces; don't grep them.
- One fix per cluster, one experiment per fix.
- New failure modes become golden items before the fix ships.
