# Writing Style: Incident and Postmortem

**Audience:** the on-call engineer at 3am, and the team a week later.

- During: what's broken, who's affected, what we're doing, when the next update is. Four lines, timestamped, no speculation.
- After: impact in one number, timeline in a table, root cause separated from trigger, actions with owners and dates.
- Blameless. Systems and gates failed, not people.
- Say plainly what the evals and monitoring missed and why.
- Every action is prevent, detect or mitigate; label it.
- End with what changes in the OS: the rule, the checklist gate, the regression case.
- Plain words. Short sentences. No em dashes.
