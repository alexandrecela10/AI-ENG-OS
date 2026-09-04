# Model / System Card: [name] v[ ]

**Owner:** [name] · **Date:** [ ] · **Approvers:** [names from `context-library/stakeholders.md`]

## What it is

- **Base model(s):** [provider, name, snapshot]
- **Modifications:** [fine-tune (data card link) / prompt (spec link) / scaffold (design doc link)]
- **Intended use:** [ ]
- **Out-of-scope use:** [ ]

## Evaluation

| Eval | Type | n | Result | CI95 | Baseline | Delta |
|---|---|---|---|---|---|---|
| | capability | | | | | |
| | safety | | | | | |
| | regression | | | | | |

Cost: [$ / 1k] · Latency: p50 [ ] / p95 [ ] · Manifests: `outputs/experiments/...`

## Safety

- **Red-team summary:** [rounds, attack categories tried, success rate before/after mitigations] (`/red-team`)
- **Refusal behavior:** precision [ ] / recall [ ] on [set]
- **Known jailbreaks still open:** [ids in failure-modes.md]
- **Policy checklist:** `{ai-eng-os}/frameworks/safety-checklist.md` completed on [date] by [name]

## Limitations and failure modes

Top failure modes with frequency on the golden set and the mitigation in place. Link `context-library/failure-modes.md`.

## Data

Datasets used (cards linked), licences, PII handling.

## Monitoring

What's tracked in production, alert thresholds, who is paged, rollback procedure (`/rollout-plan`).

## Change log

| Version | Date | Change | Eval delta |
|---|---|---|---|
