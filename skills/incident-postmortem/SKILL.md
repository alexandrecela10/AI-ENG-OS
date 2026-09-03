---
name: incident-postmortem
description: Write a blameless postmortem for a model or agent incident: impact, timeline, root cause vs trigger, why evals and monitoring missed it, actions (prevent/detect/mitigate), and the OS changes it implies.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/incident-postmortem "2026-09-01 summariser leaked internal ticket ids"
/incident-postmortem --from-traces outputs/traces/incident-2026-09-01/ --timeline slack-export.txt
```

**What you get:** `outputs/postmortems/[date]-[slug].md` from `{ai-eng-os}/templates/postmortem-template.md` in `{ai-eng-os}/voice/writing-style-incident.md` voice, plus drafted `failure-modes.md` rows, golden items, and any proposed change to launch-readiness or CLAUDE.md rules (all for approval).

**Time:** 45–60 minutes.

---

# /incident-postmortem

## Steps

1. **Impact** in one number first; then who, what they saw, cost.
2. **Timeline** from traces, alerts, chat. UTC. Source per row.
3. **Root cause vs trigger.** What changed (prompt / snapshot / data / retrieval / tool / traffic). Then the underlying gap: why the eval didn't have this case, why monitoring didn't fire, why the gate didn't stop it.
4. **Actions** typed prevent/detect/mitigate, with owner and due. Always include: regression case(s), failure-mode row, alert or gate change.
5. **Lessons for the OS.** Propose the rule, checklist gate or eval that would have prevented it; offer to open the edit.
6. **Feed forward**: `/jailbreak-regression --add-from-incident` if adversarial; `/golden-set-curate --add-regression FM-xxx` otherwise.

## Rules

- Blameless. Systems and gates, not people.
- Say plainly what was missed.
- Never close without the regression case merged or scheduled.
