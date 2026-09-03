---
name: safety-review
description: Structured safety and policy review of a system or change using the safety checklist and the safety-reviewer persona. Produces approve / approve with conditions / block with named conditions.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/safety-review outputs/design-docs/triage-agent-design.md
/safety-review --release v5                                 → review a release candidate with its eval and red-team results
```

**What you get:** `outputs/red-team/safety-review-[slug]-[date].md`: checklist with pass/fail/unknown per item, refusal precision/recall and over-refusal numbers, privacy findings, agent gate coverage, verdict and conditions with owners.

**Time:** 30 minutes.

---

# /safety-review

Adopt `{ai-eng-os}/agents/safety-reviewer.md`. Walk `{ai-eng-os}/frameworks/safety-checklist.md` section by section.

## Inputs to gather

Prompt spec (must-nevers), brief (policy lines, users), latest safety eval run (refusal P/R, over-refusal), red-team report, design doc (tools, gates, tracing), data handling notes.

## Verdict rules

- **Block**: any open critical/high red-team finding; refusal recall below floor; irreversible action without a gate; cross-tenant leakage possible; PII retention undefined.
- **Approve with conditions**: medium findings with owners and dates; monitoring gaps that can be closed before ramp.
- **Approve**: all items pass or are consciously accepted with rationale.

## Output

Verdict first. Conditions as a table (condition, owner, due). Residual risk in two plain sentences. Link everything.

## Rules

- Unknown is not pass.
- Over-refusal is a safety finding too; users routed away from help is harm.
- The named safety approver in `stakeholders.md` signs; this skill drafts.
