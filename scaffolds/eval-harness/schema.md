# Dataset schema

JSONL, one object per line.

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string | yes | stable across versions; referenced by failure modes |
| `input` | object | yes | whatever the prompt template needs |
| `expected` | object or string | for reference graders | gold answer, checklist, or schema name |
| `slice` | object | recommended | `{"lang": "en", "segment": "smb", "difficulty": "hard"}` |
| `source` | string | yes | provenance |
| `tags` | array | optional | failure-mode ids (`FM-003`), `regression`, `safety` |

Golden files are frozen: record `sha256` in the manifest and in `context-library/evals/README.md`.
