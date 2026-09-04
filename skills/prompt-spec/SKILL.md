---
name: prompt-spec
description: Write the behavior contract for a prompt before writing the prompt. Inputs, output format, must-always/must-never, refusal path, token budget, behavior examples. Registers the prompt in the prompt registry.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/prompt-spec "ticket summariser system prompt"
/prompt-spec --from outputs/design-docs/ticket-summary-design-v1.md
/prompt-spec --register             → also create prompts/[name].md v1 in the registry scaffold
```

**What you get:** `outputs/prompts/[name]-spec.md` from `{ai-eng-os}/templates/prompt-spec-template.md`; with `--register`, `outputs/scaffolds/prompt-registry/prompts/[name].md` v1 with frontmatter (model, eval, gated metrics).

**Time:** 20 minutes.

---

# /prompt-spec

A prompt without a contract can't be tested. The contract is the list of behaviors that become eval slices.

## Context routing

Design doc → structure, where context and tool results go. `project-brief.md` → model, token budget, policy lines. `failure-modes.md` → must-nevers. `{ai-eng-os}/frameworks/prompt-engineering-principles.md` → structure defaults.

## Steps

1. **Contract table.** Inputs with sizes; output format (schema or structure); must-always; must-never; refusal behavior; tone; token budget. Each row should be checkable.
2. **Structure.** system / developer / context / user with what goes where. Context and tool results delimited and labelled as data.
3. **Behavior examples.** Happy path, ambiguous, out of scope, injection in context, empty input. These become the first golden items.
4. **Register** (if asked): create `prompts/[name].md` with frontmatter `name, version: v1, model: <pinned snapshot>, eval, grader, gated_metrics, owner, changelog`. Body is the first draft of the prompt following the principles.
5. **Hand off**: `/eval-spec` if no eval covers this contract; `/prompt-iterate` for the first improvement.

## Rules

- Every must-never gets an eval item.
- Pinned snapshot in the frontmatter.
- No "be accurate" or "don't hallucinate" lines. Give sources and a refusal path instead.
