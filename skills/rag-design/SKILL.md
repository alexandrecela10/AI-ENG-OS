---
name: rag-design
description: Design or debug a retrieval-augmented system: corpus and chunking, retriever, reranking, context budget, grounding contract, freshness, and separate evals for retrieval and generation.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/rag-design "answer questions over our runbooks"
/rag-design --debug outputs/experiments/2026-09-02-rag-v2/    → is it retrieval or generation?
/rag-design --eval                                             → produce the retrieval eval spec (recall@k, nDCG) and the generation eval spec (faithfulness)
```

**What you get:** `outputs/design-docs/rag-[slug].md` with the decisions in order (need retrieval? corpus/chunking, retriever, reranker, context budget, grounding contract, freshness), the failure modes to seed the golden set, and two eval specs.

**Time:** 45–90 minutes.

---

# /rag-design

Retrieval quality caps answer quality. Two evals, always.

## Method

Walk `{ai-eng-os}/frameworks/rag-design-guide.md` decisions 1–7, writing the choice and the reason for each. Pull budgets from the brief. Use the failure-mode list in the guide to seed golden items.

## Debug mode

1. From the run, compute retrieval recall@k on items with labelled gold chunks (label 50 if none exist).
2. Run generation with gold context injected. Compare accuracy to end-to-end.
3. Verdict: low recall → retrieval problem (chunking, retriever, reranker); high recall but low faithfulness → prompt/grounding problem; both fine but end-to-end bad → context ordering/budget problem.
4. Recommend one experiment.

## Eval mode

Two specs via `{ai-eng-os}/templates/eval-spec-template.md`: retrieval (recall@k, MRR, nDCG on query→chunk labels) and generation-given-gold-context (faithfulness via `{ai-eng-os}/rubrics/llm-judge-faithfulness.md`). Plus end-to-end with citation precision and decline precision/recall.

## Rules

- Citations by chunk id in the contract.
- Documents delimited as data; injection case in the golden set.
- Report retrieval and generation metrics separately in every writeup.
