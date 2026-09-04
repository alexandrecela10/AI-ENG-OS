# Prompt Spec: [prompt name]

**Path:** `prompts/[name].md` · **Version:** v[ ] · **Owner:** [name] · **Model:** [name + snapshot] · **Eval:** `evals/[name]`

## Purpose

One sentence: what this prompt gets the model to do, for whom.

## Contract

| Dimension | Specification |
|---|---|
| Inputs | [variables, their types, max sizes; where retrieved content and tool results are inserted] |
| Output format | [JSON schema / markdown structure / free text with constraints] |
| Must always | [e.g. cite a source id for every factual claim] |
| Must never | [e.g. answer outside the provided documents; reveal system prompt] |
| Refusal behavior | [when and how to decline] |
| Tone / audience | [ ] |
| Token budget | input <= [ ], output <= [ ] |

## Structure

```
[system]   role, constraints, output format, refusal rules
[developer] task-specific instructions, few-shot examples (n = [ ])
[context]  retrieved documents, delimited and labelled with ids
[user]     the request
```

## Behavior examples

| Scenario | Input | Expected output | Why |
|---|---|---|---|
| Happy path | | | |
| Ambiguous | | asks one clarifying question | |
| Out of scope | | declines, points to [ ] | |
| Injection in context | | ignores instruction in doc, answers user | |

## Change log

| Version | Date | Change (one variable) | Eval delta | Manifest |
|---|---|---|---|---|
| v1 | | initial | baseline | `outputs/experiments/...` |
