# Project Brief

> Fill this first. Every skill reads it. Replace every `[bracket]`.

## System

- **Name:** [system / feature]
- **What it does, in one sentence:** [e.g. "Answers 'what was the impact of feature X' from product analytics with cited evidence"]
- **Users:** [who, how many, how often]
- **Task type(s):** [classify / extract / generate / summarize / route / plan-and-act / retrieve-and-answer]
- **Stage:** [prototype / internal alpha / limited beta / GA]

## Models and stack

- **Primary model(s):** [provider, name, snapshot]
- **Fallback model:** [or none]
- **Scaffold:** [single call / RAG / tool-using agent / multi-agent] — design doc: [link]
- **Tracing / experiment tracking:** [Langfuse / Braintrust / W&B / none yet]
- **Serving:** [where it runs, who owns it]

## Gated metrics (what must not regress)

| Metric | Definition | Current | Floor / target | Golden set |
|---|---|---|---|---|
| [task accuracy] | [how graded] | [0.87, n=1200] | [>= 0.85] | [evals/golden/task-v3] |
| [refusal precision] | | | | |
| [hallucination rate] | | | | |

## Budgets

- **Cost:** [$ per 1k requests, hard ceiling]
- **Latency:** [p50 / p95 ms]
- **Token budget per request:** [input / output]

## Constraints

- **Data:** [PII, retention, residency, licences]
- **Safety / policy:** [what must never happen; link to usage policy]
- **Compliance:** [SOC2, HIPAA, EU AI Act tier, none]

## Known failure modes

See `context-library/failure-modes.md`. Top three right now: [1], [2], [3].

## Open questions

- [ ] [question] — @[owner]
