# Postmortem: [title]

**Severity:** SEV[1-4] · **Owner:** [name] · **Date of incident:** [ ] · **Duration:** [ ] · **Status:** Draft / Reviewed

## Impact

Who was affected, how many requests / users, what they saw, cost incurred. One number that matters most.

## Timeline (UTC)

| Time | Event | Source |
|---|---|---|
| | first bad output | trace link |
| | alert fired / user report | |
| | mitigation | |
| | resolved | |

## Root cause

What actually changed (prompt / model snapshot / data / retrieval / tool / traffic). Why the evals and gates didn't catch it. Distinguish trigger from underlying cause.

## What went well / what didn't

## Actions

| Action | Type (prevent / detect / mitigate) | Owner | Due | Ticket |
|---|---|---|---|---|
| add regression case(s) to golden set | prevent | | | |
| add failure mode FM-[ ] | prevent | | | |
| add alert on [ ] | detect | | | |
| add gate to launch readiness | prevent | | | |

## Lessons for the OS

What rule, checklist item or eval would have prevented this. Offer to update `CLAUDE.md`, `launch-readiness-template.md` or `failure-modes.md`.
