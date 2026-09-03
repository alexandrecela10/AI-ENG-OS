# data-pipeline

Filter → dedupe → PII scrub → (label) → dataset card, with row counts logged at every step so a 90% drop is visible.

```
data-pipeline/
├── pipeline.py   # python pipeline.py --in raw.jsonl --out clean.jsonl --report report.json
└── README.md
```

Steps are plain functions taking and returning lists of dicts; add, remove or reorder. Near-dup uses a cheap shingle Jaccard; swap for MinHash or embeddings when the set is large. PII scrub is regex-only; use a proper detector for anything that leaves the team.

The report feeds `/dataset-card` (counts in → out per step, dup rate, PII hit rate, length distribution).
