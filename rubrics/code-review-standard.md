# Code Review Standard (model-backed systems)

Additions to normal code review when a PR touches prompts, models, retrieval, tools or evals.

## Always

- [ ] Prompt changes come with an eval delta (manifest linked in the PR) or are labelled "no behavior change" with a regression run proving it.
- [ ] Model snapshot pinned; any bump is its own PR with its own eval.
- [ ] Prompts live in the registry (`prompts/`), not inline strings; version bumped; change log entry.
- [ ] Every model call is traced (inputs, outputs, tokens, cost, latency, version ids).
- [ ] Temperature 0 and seed for anything parsed or evaluated.
- [ ] Output parsing tolerates the model being wrong (schema validation, one retry, then fail closed).
- [ ] Token, step, dollar and wall-clock caps present in any loop.
- [ ] Side-effecting tools go through the human gate; read-only tools are marked as such.
- [ ] Retrieved content and tool results are delimited as data in the prompt.
- [ ] No secrets, PII or full prompts in logs beyond the retention policy.
- [ ] Golden set files are hash-checked in CI; changes to golden need a reviewer from `stakeholders.md`.

## Evals in CI

- [ ] Regression suite runs on the PR (or nightly with the PR referenced) and the delta table is posted as a comment.
- [ ] Failing gated metric blocks merge.

## Ask in review

"What's the baseline?" · "Which failure mode does this address, and is there a regression case?" · "What happens on tool error?" · "How do we roll this back?"
