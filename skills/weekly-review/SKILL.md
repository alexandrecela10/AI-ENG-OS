---
name: weekly-review
description: End-of-week review of the experiment log: what moved, calibration of predictions vs results, failure modes opened and closed, what to try next, and proposed updates to the OS (rules, templates, golden set).
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/weekly-review
/weekly-review --since 2026-08-25
```

**What you get:** `outputs/weekly-reviews/[date].md` and proposed diffs (for approval) to `context-library/ai-eng-os-learning-log.md`, `failure-modes.md` and, if patterns warrant, `CLAUDE.md` rules or templates.

**Time:** 20 minutes.

---

# /weekly-review

## Gather

All manifests since the last review; writeups; reviews; incidents; regression runs; status of golden set (size, last refresh).

## Sections

1. **Metric movement** on gated metrics with CIs; what caused it.
2. **Experiments**: promoted / iterated / discarded, one line each, with the lesson.
3. **Calibration**: predicted vs actual per change type. Over-optimistic on prompts? Under on retrieval? Say so with numbers.
4. **Failure modes**: opened, closed (with regression case ids), oldest open.
5. **Eval health**: golden size, last contamination check, judge calibration date, regression suite runtime.
6. **Budget**: cost/1k and p95 trend vs budget.
7. **Next week**: ranked experiments, one variable each.
8. **OS updates**: patterns worth a rule; templates that needed the same edit twice; skills that were awkward. Propose the edits.

## Rules

- Propose OS edits; never apply silently.
- Discards are learning; count them.
