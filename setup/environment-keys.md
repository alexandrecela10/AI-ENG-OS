# Environment Keys

What needs a key, what doesn't, and how to keep keys out of the repo.

## Nothing needs a key to install

Installing the plugin, running `/ai-init`, writing specs, design docs, writeups, reviews and plans: all file work. No provider key required.

## What needs a model key

| Activity | Needs | Where it's read |
|---|---|---|
| Running the eval harness against a model | your provider key | your project's model client, called from `harness.call_model()` |
| LLM-as-judge grading | a key for the **judge** model (fixed, ideally a different family from the system under test) | `graders/llm_judge.py` via the `call_model` you pass in |
| Agent loop scaffold | provider key | `loop.call_model()` stub |
| `/prompt-regression` in CI | provider key as a CI secret | `test_prompts.py` → your harness |
| `/red-team` automated attempts | provider key | your harness |

## What needs a tool key (optional)

| Tool | Skills that benefit | Key |
|---|---|---|
| Langfuse / Braintrust / W&B | `/eval-run-report`, `/trace-debug`, `/weekly-review` | tracing/tracking API key |
| Hugging Face | `/dataset-card`, `/literature-scan`, `/finetune-plan` | HF token (read) |
| GitHub | `/prompt-regression --setup-ci`, `/changelog` | already via Devin's integration |
| Linear / Slack / Datadog | tickets, status delivery, incident timelines | per tool |

Connect with `/connect-mcps connect to <tool>`. All skills fall back to files if nothing is connected.

## Rules

1. **Env vars or a secret store only.** Never in a prompt file, manifest, notebook or `outputs/`. `.env` is gitignored by the plugin's `.gitignore`; add the same to your project.
2. **Name keys descriptively.** `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `LANGFUSE_SECRET_KEY`, `HF_TOKEN`. In Devin Cloud, store them as session or repo secrets; in CI, as repository secrets.
3. **Separate judge and subject.** If you can, use a different account or at least a different model for the judge so cost and rate limits are visible separately and self-preference is reduced.
4. **Pin snapshots.** Keys select the provider; the manifest pins the model snapshot (e.g. `claude-sonnet-4-5@2025-09-29`). Both matter for reproducibility.
5. **Budget caps.** Set spend alerts at the provider. The agent loop's `Caps.max_usd` is a per-run guard, not a monthly one.

## Devin Cloud

Secrets → https://app.devin.ai/settings/secrets (org or repo scope). Reference by name in code; Devin injects them into the shell. Never `echo` a secret in a session transcript.

## Devin CLI / Claude Code (local)

```bash
export ANTHROPIC_API_KEY=...          # or use direnv / 1Password CLI / your shell's secret manager
```
Or put it in `~/.config/ai-eng-os/env` and `source` it; keep it out of every repo.

## Checking without leaking

```bash
test -n "$ANTHROPIC_API_KEY" && echo "set" || echo "missing"
```
