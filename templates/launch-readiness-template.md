# Launch Readiness: [system / change] v[ ]

**Owner:** [name] · **Target date:** [ ] · **Approvers (human gate):** [names] · **Decision:** GO / NO-GO / GO with conditions

## Evidence

| Gate | Requirement | Evidence | Status |
|---|---|---|---|
| Gated evals | every gated metric >= floor; no drop beyond CI | manifest links | ☐ |
| Eval validity | `/eval-review` passed, judge calibrated, golden set frozen | | ☐ |
| Safety | red-team round complete, no open critical/high | report link | ☐ |
| Regression | prompt/jailbreak regression suite green on release candidate | | ☐ |
| Cost | projected $/1k <= budget at expected volume | | ☐ |
| Latency | p95 <= budget under load test | | ☐ |
| Tracing | every inference traced; dashboards live | | ☐ |
| Monitoring | alerts on gated metrics, cost, p95, error rate; thresholds set | | ☐ |
| Rollback | one-command rollback tested; owner named; kill switch tested | | ☐ |
| Rollout plan | canary %, promotion criteria, duration | `/rollout-plan` link | ☐ |
| Data / privacy | PII handling reviewed; retention set | | ☐ |
| Docs | model card updated; changelog entry; runbook | | ☐ |
| Comms | users / support / on-call informed | | ☐ |

## Known risks accepted

| Risk | Likelihood | Impact | Why acceptable | Owner |
|---|---|---|---|---|

## Conditions (if GO with conditions)

- [ ] [condition] — @[owner] — by [date]

## Sign-off

| Approver | Decision | Date |
|---|---|---|
