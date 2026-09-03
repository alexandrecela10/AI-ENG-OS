---
name: tool-schema
description: Write or review tool schemas the model can use reliably: names, descriptions, typed parameters, error shapes, side-effect flags, plus a 20-case selection test.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/tool-schema "search_orders, get_order, refund_order"
/tool-schema --review src/tools/*.py             → review existing schemas against the guidelines
/tool-schema --test                              → generate the should-call / shouldn't-call test set
```

**What you get:** `outputs/design-docs/tools-[slug].md` with each schema (JSON), the read-only/side-effecting flag, error shapes, and a 20-item selection test in harness format under `outputs/evals/tool-selection-[slug].jsonl`.

**Time:** 20–40 minutes.

---

# /tool-schema

## Method

Apply `{ai-eng-os}/frameworks/tool-schema-guidelines.md`:

1. **Name**: verb-noun, one job. Flag overlaps between tools.
2. **Description**: what it returns; when to use and not; side effects; units, formats, limits.
3. **Parameters**: typed, required/optional, enums, example values. No params the model can't know.
4. **Results**: compact, structured, ids for follow-ups, truncation marker. Errors as data with a hint.
5. **Flag**: `read_only: true|false`. Side-effecting → human gate.
6. **Test set**: 10 natural requests that should call it (with expected args), 10 near-misses that shouldn't (should call another tool or answer directly). Format for the harness with grader `json_schema` on the tool call.

## Review mode

For each existing schema: table of findings (naming, description, params, results, safety) with severity and a rewritten schema. Note which tools overlap and the expected selection confusion.

## Rules

- Descriptions are prompts. Write them for the model, not for the docs site.
- Re-run the selection test whenever a tool is added; selection accuracy on old tools can drop.
