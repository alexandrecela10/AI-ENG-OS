# Rubric: Faithfulness (grounded generation)

**Version:** v1 · **Use with:** a fixed judge model at temperature 0. Calibrate against human labels before gating (`/judge-calibrate`).

## Judge prompt

```
You are grading whether an ANSWER is supported by the provided CONTEXT. Do not use outside knowledge. Do not reward length or style.

Steps:
1. Split the ANSWER into atomic factual claims. List them.
2. For each claim, mark SUPPORTED (directly stated or clearly entailed by CONTEXT), UNSUPPORTED (not in CONTEXT), or CONTRADICTED (CONTEXT says otherwise). Quote the supporting or contradicting span.
3. If the ANSWER declines because the CONTEXT lacks the information, and the CONTEXT does lack it, grade 5.

Score:
5 = all claims SUPPORTED, or a correct decline
4 = all claims SUPPORTED except one minor unsupported detail that doesn't change the meaning
3 = one substantive UNSUPPORTED claim, none CONTRADICTED
2 = multiple UNSUPPORTED claims, or one CONTRADICTED
1 = the main claim is UNSUPPORTED or CONTRADICTED

Return JSON: {"claims":[{"text":"","verdict":"SUPPORTED|UNSUPPORTED|CONTRADICTED","evidence":""}],"score":1-5,"reason":"one sentence"}
```

## Aggregation

Report mean score, share of 5s, share of ≤2 (the hallucination rate). Report per slice.

## Known biases

Judges under-penalise plausible paraphrase; over-penalise correct inference that isn't verbatim. Calibrate and report κ.
