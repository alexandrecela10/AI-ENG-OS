# Scaffolds

Runnable starters. Skills copy a scaffold into the working repo (`outputs/scaffolds/<name>/` first, then wherever the engineer moves it) and adapt it. The working repo owns its copy; nothing here is imported at runtime.

| Scaffold | What it gives you | Copied by |
|---|---|---|
| `eval-harness/` | dataset schema (JSONL), grader interface, exact/JSON/LLM-judge graders, bootstrap CIs, results table, manifest writer | `/eval-build` |
| `prompt-registry/` | versioned prompt files with hashes, a loader, and a test file that runs the golden set | `/prompt-spec`, `/prompt-iterate` |
| `agent-loop/` | tool registry with schemas, loop with step/token/dollar caps, tracing hooks, human gate | `/agent-design` |
| `data-pipeline/` | filter → dedupe → PII scrub → label → card, with counts at each step | `/data-quality-audit`, `/synthetic-data-plan` |

All Python, standard library plus whatever model SDK the project already uses. Model calls are behind a single `call_model()` function you replace.
