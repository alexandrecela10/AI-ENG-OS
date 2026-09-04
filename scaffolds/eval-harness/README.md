# eval-harness

Minimal, dependency-light eval harness. Copy, then replace `call_model()` in `harness.py` with the project's model client.

```
eval-harness/
├── harness.py          # run: python harness.py --dataset golden.jsonl --grader exact --out outputs/experiments/<id>/
├── graders/
│   ├── base.py         # Grader interface
│   ├── exact.py        # normalised exact match
│   ├── json_schema.py  # output parses and matches schema
│   └── llm_judge.py    # rubric-based judge, temperature 0, returns score + reason
├── rubrics/            # copy rubrics from {ai-eng-os}/rubrics/ here
├── stats.py            # bootstrap CI, Wilson interval, paired delta CI
└── schema.md           # dataset JSONL schema
```

## Dataset schema (`schema.md`)

One JSON object per line:

```json
{"id": "task-0001", "input": {...}, "expected": {...}, "slice": {"lang": "en", "difficulty": "hard"}, "source": "prod-sample-2026-08", "tags": ["FM-003"]}
```

## Run

```bash
python harness.py --dataset evals/golden/task-v3.jsonl --grader exact --model claude-sonnet-4-5 --prompt prompts/system.md --out outputs/experiments/2026-09-03-v4/
```

Writes `results.jsonl` (per item), `summary.json` (metrics with CIs, cost, latency, per slice) and a pre-filled `manifest.json` you complete with hypothesis, baseline and decision.
