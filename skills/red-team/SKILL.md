---
name: red-team
description: Plan and run a red-team round against a prompt, model or agent using the attack taxonomy, then write the report with findings, mitigations, re-test results and the regression cases to add.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/red-team prompts/assistant.md@v5                     → plan a round against the behavior contract
/red-team --agent outputs/design-docs/triage-agent-design.md   → focus on tool results and gated actions
/red-team --report outputs/red-team/round-3-findings.jsonl     → write the report from logged attempts
```

**What you get:** a plan (`outputs/red-team/[slug]-round-[n]-plan.md`: categories, budget per category, success criteria, adjudicator) and after the round a report from `{ai-eng-os}/templates/red-team-report-template.md`, plus drafted regression items and `failure-modes.md` rows for approval.

**Time:** 30 minutes to plan; a round is hours to days.

---

# /red-team

Adopt `{ai-eng-os}/agents/red-teamer.md`. Scope is defensive: find the failures so they can be fixed.

## Plan

1. **Targets**: every must-never in the prompt spec and every prohibited use in the brief.
2. **Taxonomy**: walk `{ai-eng-os}/frameworks/safety-checklist.md` § attack taxonomy; add project-specific categories.
3. **Budget**: attempts per category, human vs automated, time box.
4. **Success criterion** per category and who adjudicates borderline outputs.
5. **Logging**: every attempt as `{category, attack_summary, result, severity, trace_id}` in `outputs/red-team/…jsonl`.

## Report

Fill the template: findings table by severity, mitigations with coverage, re-test deltas on gated metrics, residual risk, regression additions.

## Rules

- Describe attack classes in shared docs; keep genuinely dangerous payloads in the restricted eval set only.
- Every successful attack becomes a regression case before the mitigation ships.
- Re-test on the mitigated version; report gated metrics too (mitigations can cause over-refusal).
- Open critical/high findings block launch readiness.
