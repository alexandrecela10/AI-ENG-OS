---
name: stats-uncertainty-report
description: Rewrite any table or paragraph of numbers to the OS uncertainty standard: CIs, n, paired deltas, verdict language, exec translation. Stats pack.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/stats-uncertainty-report outputs/status-updates/2026-09-05.md
/stats-uncertainty-report --table "v4 0.81, v5 0.91, n=412 paired, 62 discordant"
/stats-uncertainty-report --exec
```

**What you get:** the same document or table rewritten per `{ai-eng-os}/domains/stats/frameworks/uncertainty-reporting.md`: every number with CI and n, deltas paired where applicable, "significant" replaced with verdict language, and (with `--exec`) the plain-language translation.

**Time:** 5–10 minutes.

---

# /stats-uncertainty-report

## Steps

1. Find every number that's a measurement. Attach n and CI (compute where the data or counts are available: Wilson for proportions, bootstrap for means and paired deltas).
2. Find every comparison. Make it a difference with its CI; mark paired/unpaired.
3. Replace banned words (`uncertainty-reporting.md` table).
4. Count the comparisons; flag if multiplicity isn't addressed.
5. `--exec`: translate each CI into "about X, give or take Y" and keep the caveat.
6. Re-read the original file and apply only these changes; don't regenerate.

## Rules

- Never remove a caveat to make a sentence shorter.
- If a CI can't be computed from what's in the doc, write "[CI not reported]" rather than inventing one.
