---
name: decision-doc
description: Record an engineering decision (model choice, architecture, eval methodology, build vs buy) with context, options, evidence, consequences and the metric that would reopen it.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/decision-doc "use sonnet for summarisation, haiku for routing"
/decision-doc --from outputs/experiments/2026-09-03-routing/    → decision backed by an experiment
/decision-doc --rfc                                             → produce an RFC for comment first
```

**What you get:** `outputs/decisions/[date]-[slug].md` from `{ai-eng-os}/templates/decision-template.md`; with `--rfc`, `outputs/decisions/rfc-[slug].md` from `{ai-eng-os}/templates/rfc-template.md`.

**Time:** 15 minutes.

---

# /decision-doc

## Steps

1. **Context**: what forced the decision; numbers; deadline.
2. **Options** table with evidence for/against (link manifests, lit scan), cost and risk.
3. **Decision** in one present-tense sentence.
4. **Consequences**: easier, harder, committed to.
5. **Reopen condition**: the metric and threshold that would make us revisit.
6. Check `context-library/decisions/` for a prior decision this supersedes; link it.

## Rules

- Evidence links, not adjectives.
- Every decision has a reopen condition.
- If PM OS is installed and the decision is product-facing, offer `/pm-os:decision-doc` for the product record too.
