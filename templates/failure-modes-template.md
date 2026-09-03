# Failure Modes

> Living catalogue. Every skill checks it before proposing a change; `/trace-debug` and `/incident-postmortem` append to it (with your approval). Each entry should have a regression case in the golden set.

| ID | Failure mode | Symptom | First seen | Root cause (if known) | Regression case | Status |
|---|---|---|---|---|---|---|
| FM-001 | [e.g. Fabricated citation] | [model cites a doc id that doesn't exist in retrieval results] | [date, trace link] | [retrieval returned 0 docs; prompt had no "say you don't know" path] | [evals/golden/task-v3#217-231] | open / mitigated / closed |

## Categories (seed list, see `{ai-eng-os}/frameworks/failure-mode-catalogue.md`)

Hallucination · Over-refusal · Under-refusal · Instruction drift in long context · Tool misuse · Infinite loop / budget blowout · Format violation · Prompt injection via retrieved content · Stale retrieval · Bias / disparate performance · Latency tail · Cost spike
