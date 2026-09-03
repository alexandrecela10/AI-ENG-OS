# Failure Mode Catalogue (seed)

Starting taxonomy for `context-library/failure-modes.md`. Each project keeps its own instances with trace links and regression cases; this is the shared vocabulary.

| Category | Typical symptom | Usual cause | First mitigation to try | Regression case shape |
|---|---|---|---|---|
| **Hallucination / fabrication** | confident claim not in sources | no refusal path; weak retrieval; prompt asks for completeness | grounding contract + cite-by-id + "say you don't know" | question whose answer isn't in the corpus |
| **Over-refusal** | declines benign request | broad safety instruction; judge over-weighting caution | benign look-alike examples in prompt; measure refusal precision | benign request near a policy line |
| **Under-refusal** | complies with prohibited request | missing category in policy prompt; injection | explicit prohibited list + examples; classifier pre-check | adversarial request per category |
| **Instruction drift** | ignores system rules late in long context | long context; rules buried mid-prompt | move rules to start and end; compact history | 30-turn conversation with a late rule test |
| **Format violation** | invalid JSON, missing fields | no example; sampling temperature | schema in prompt + example + parser retry once | 20 varied inputs, schema check |
| **Prompt injection via data** | follows instructions found in a document or tool result | context not delimited as data | wrap data, say it's untrusted, strip imperative text | doc containing "ignore previous instructions" |
| **Tool misuse** | wrong tool, wrong args, loops | overlapping tools; vague descriptions | fewer tools, better schemas (`/tool-schema`) | 10 should-call / 10 shouldn't-call requests |
| **Budget blowout** | runaway steps or tokens | no caps; reflection loop | step/token/dollar caps; fail closed | task designed to be unsolvable |
| **Stale retrieval** | answers from superseded doc | no recency signal; index lag | recency in ranking; supersession metadata | two docs, one superseding the other |
| **Verbosity / padding** | long answers, low density | no length target; judge length bias | length target in prompt; length-normalised judge | short-answer questions |
| **Sycophancy** | agrees with user's wrong premise | RLHF prior; no instruction to correct | "correct false premises" instruction; examples | questions with false premises |
| **Bias / disparate performance** | accuracy varies by group or language | skewed data; single-language prompts | per-slice eval; targeted data | slices in golden set |
| **Latency tail** | p95 spikes | long outputs; retries; provider variance | output caps; timeouts; fallback model | load test with long inputs |
| **Silent model update** | metrics shift with no code change | unpinned model | pin snapshot; nightly drift eval | scheduled golden run |
| **Cost spike** | daily spend jumps | traffic shape; caching miss; agent loops | alerts; cache prefix; caps | synthetic traffic replay |

## Using the catalogue

When `/trace-debug` clusters failures, map each cluster to a category here, then create a project-specific FM-id in `failure-modes.md` with the trace links and the regression case ids. Closed failure modes stay in the golden set forever.
