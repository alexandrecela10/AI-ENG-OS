# Monitoring Plan: [model] v[ ]

**Owner / on-call:** [ ] · **Dashboards:** [links] · **Retraining owner:** [ ]

## What we watch

| Signal | Metric | Threshold | Window | Alert to | Action |
|---|---|---|---|---|---|
| input drift | PSI / KL per key feature vs training window | | daily | | investigate; consider retrain |
| prediction drift | score distribution shift | | daily | | |
| performance (when labels arrive) | primary metric on labelled sample | below floor [ ] | weekly | | rollback / retrain |
| calibration | expected vs observed by bin | | weekly | | recalibrate |
| slice performance | primary metric per segment | any slice below [ ] | weekly | | |
| data quality | null rate, schema, range violations | | hourly | | block scoring |
| latency / cost | p95, $/1k | budget | realtime | | |

## Label latency

How long until ground truth is known: [ ]. Proxy metric until then: [ ].

## Retraining

Trigger (schedule / drift / performance); data window; validation before promote (same golden test, hash); rollback path.

## Human review

Sample [n]/week read by [who]; findings feed `failure-modes.md`.
