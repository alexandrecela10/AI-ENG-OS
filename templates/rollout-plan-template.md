# Rollout Plan: [change] v[ ]

**Owner:** [name] · **On-call during rollout:** [name] · **Kill switch:** [how, who, tested on date]

## Strategy

shadow → canary [ ]% → [ ]% → 100%, or A/B with [ ]% treatment for [duration]. Why this shape (see `{ai-eng-os}/frameworks/rollout-strategies.md`).

## Stages

| Stage | Traffic | Duration | Promote if | Roll back if | Owner |
|---|---|---|---|---|---|
| shadow | 0% (log only) | | outputs match on [ ]% of [ ] sampled | | |
| canary | [ ]% | | gated metrics within CI of baseline; p95 <= [ ]; error rate <= [ ]; cost <= [ ] | any gated metric below floor; alert [ ] fires | |
| ramp | [ ]% | | | | |
| full | 100% | | | | |

## Monitoring during rollout

Dashboards: [links]. Alerts: [list with thresholds]. Sampling for human review: [n per hour, who].

## Rollback

Command / toggle: [ ]. Time to roll back: [ ]. Data implications: [ ]. Last tested: [ ].

## Comms

Before: [who]. During: [channel]. After: changelog entry (`/changelog`).
