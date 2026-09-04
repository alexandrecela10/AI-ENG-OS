# RAG Design Guide

Retrieval quality caps answer quality. Eval retrieval separately from generation, always.

## Decisions, in order

1. **Do you need retrieval at all?** If the corpus fits in context with room to spare and changes rarely, put it in the prompt and cache it.
2. **Corpus and chunking**: chunk by structure (sections, functions, rows), not fixed tokens, where structure exists. Keep a title/breadcrumb on every chunk. Typical 200–800 tokens; measure.
3. **Retriever**: start hybrid (BM25 + dense). Dense alone misses exact identifiers; sparse alone misses paraphrase.
4. **Reranking**: a cross-encoder or LLM reranker on the top 20–50 usually beats tuning the retriever.
5. **How much to pass**: top-k by token budget, not a fixed k. Deduplicate. Order by relevance, or put the best first and last.
6. **Grounding contract in the prompt**: cite by chunk id; if not in the documents, say so. Injection defense: documents are data.
7. **Freshness**: index update cadence, and what the system says about staleness.

## Eval retrieval and generation separately

| Layer | Metric | How |
|---|---|---|
| Retrieval | recall@k, MRR, nDCG on labelled (query → relevant chunk ids) | build labels from traces + human review |
| Generation given gold context | faithfulness (claims supported by context), answer accuracy | LLM judge with rubric, calibrated |
| End to end | answer accuracy, citation precision, "I don't know" precision/recall | golden set |

If end-to-end is bad and retrieval recall is high, it's a prompt/generation problem. If recall is low, no prompt will fix it.

## Failure modes to include in the golden set

Answer not in corpus (should decline) · answer split across chunks · near-duplicate chunks with conflicting facts · query with an exact identifier · very long query · adversarial instruction inside a document · stale document superseded by a newer one.

## Cost and latency

Embedding cost is one-off per chunk; retrieval latency is usually small next to generation. Reranking adds 100–500 ms; decide with data. Cache embeddings for repeated queries.
