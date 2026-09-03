# Rollout Strategies

Pick the cheapest strategy that gives the evidence you need. Every rollout has a written rollback and a named owner.

| Strategy | What it is | Evidence it gives | Use when |
|---|---|---|---|
| **Shadow** | new version runs on real traffic, outputs logged, not shown | agreement rate with prod, cost, latency, crash rate; no user risk | any model/prompt change before exposure |
| **Canary** | small % of users get the new version | live gated metrics at low blast radius | after shadow, before ramp |
| **Ramp** | canary → 10 → 50 → 100 with hold periods | trend under increasing load | default path to 100% |
| **A/B** | randomised split held for a fixed period | causal estimate of user-visible impact with CI | when the question is "did users benefit", not "did it break" |
| **Interleaving** | both versions answer, user sees one or both, preference logged | fast preference signal | ranking / search / suggestion UIs |
| **Feature flag by segment** | internal → beta cohort → all | qualitative feedback first | new capabilities with UX change |
| **Blue/green** | full switch with instant revert | speed of rollback | infra changes with no gradual option |

## Promotion criteria (write them before starting)

- Gated eval metrics on sampled live traffic within CI of baseline.
- p95 latency and error rate within budget.
- Cost per 1k within budget.
- No new failure modes in human-reviewed sample (n per stage).
- Hold period long enough to cover the traffic cycle (usually at least one full day, often a week).

## Rollback triggers

Any gated metric below floor · alert on harmful-output rate · p95 or error rate over budget for [x] minutes · cost anomaly · on-call judgement. Rollback is one action, tested before the rollout starts.

## Model-specific gotchas

- Provider model updates are a rollout you didn't schedule. Pin snapshots; treat a snapshot bump as a change with its own canary.
- Prompt caching changes cost profiles at different traffic levels; check cost at each ramp stage.
- Agents: watch step counts and budget exhaustion rate as leading indicators.

## After

`/changelog` entry, model card update, calibration note (predicted vs actual impact) in the learning log.
