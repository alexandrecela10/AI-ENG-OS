---
name: design-doc
description: Write an engineering design doc for a model-backed system or change. Constraints first, explicit prompt/tool/retrieval/loop design, alternatives, eval plan, failure modes, rollout. Offers a reviewer panel.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/design-doc "ticket summariser v1"
/design-doc --from outputs/design-docs/ticket-summary-framing.md
/design-doc --review                        → run infra-reviewer, safety-reviewer, eval-skeptic on the draft
```

**What you get:** `outputs/design-docs/[slug]-design-v1.md` from `{ai-eng-os}/templates/design-doc-template.md`, in `{ai-eng-os}/voice/writing-style-design-doc.md` voice.

**Time:** 1–2 hours.

---

# /design-doc

## Context routing

Framing doc → problem and metric. `project-brief.md` → stack, budgets. `decisions/` → settled choices. `failure-modes.md` → risks section. `{ai-eng-os}/frameworks/agent-design-patterns.md` → pick the lowest rung on the ladder that works. `{ai-eng-os}/frameworks/rag-design-guide.md`, `tool-schema-guidelines.md`, `cost-latency-budgeting.md`, `rollout-strategies.md` for the relevant sections.

## Steps

1. **Constraints first.** Pull budgets and policy lines into section 2 before writing any design.
2. **Design at the lowest viable level** of the agent ladder. Justify each step up.
3. **Be concrete about the model parts**: model + snapshot, decoding config, prompt structure with where context and tool results go, tool list, retrieval settings, loop caps, human gate, tracing fields.
4. **Alternatives** including "do nothing" and "no model", each with a real con.
5. **Eval plan**: link the spec; state the delta that would justify shipping and the result that would stop the project.
6. **Failure modes**: from the catalogue and the project list; each with detection, mitigation, owner.
7. **Rollout**: shape, promotion criteria, rollback owner.
8. **Open questions** with owners.

## Review (`--review` or on request)

Run `{ai-eng-os}/agents/infra-reviewer.md`, `safety-reviewer.md`, `eval-skeptic.md`, and `user-advocate.md` against the draft. Summarise blocking vs non-blocking findings at the top of the doc under "Review notes". Offer `/ai-review-panel` for a full panel.

## Rules

- Every behavioral claim points at an eval or says "unmeasured".
- Caps (steps, tokens, dollars, time) are design decisions, written down.
- Two pages before appendix. Diagrams for flow, prose for rationale.
