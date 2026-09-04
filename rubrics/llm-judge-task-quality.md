# Rubric: Task Quality (reference-guided)

**Version:** v1 · **Use with:** a reference answer or a checklist of required elements. Judge at temperature 0.

## Judge prompt

```
You are grading a RESPONSE to a TASK against a REFERENCE (a gold answer or a checklist of required elements). Grade content, not style. Do not reward length.

1. Correctness: does the RESPONSE reach the same conclusion / contain the required elements? List each required element and mark PRESENT / MISSING / WRONG.
2. Completeness: are any required elements missing?
3. Precision: does the RESPONSE add claims that are wrong or irrelevant?
4. Format: does it follow the requested format exactly?

Score 1–5:
5 = all elements PRESENT, nothing WRONG, format correct
4 = all elements PRESENT, minor irrelevant addition or minor format slip
3 = one element MISSING or one minor WRONG element
2 = multiple MISSING, or one substantive WRONG element
1 = conclusion wrong or most elements MISSING

Return JSON: {"elements":[{"name":"","status":"PRESENT|MISSING|WRONG"}],"format_ok":true|false,"score":1-5,"reason":"one sentence"}
```

## Aggregation

Mean, share of ≥4 (pass rate), per-slice. Pair with an exact/code check where one exists; use the judge for what code can't check.
