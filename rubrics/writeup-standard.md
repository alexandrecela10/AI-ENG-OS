# Writeup Standard

What a reviewer checks before an experiment writeup, design doc or postmortem is accepted. Used by `/experiment-writeup`, `/ai-review-panel`, `research-scientist` persona.

## Must have

- [ ] TL;DR in three sentences: change, effect with CI, next step.
- [ ] Hypothesis with a predicted number, and the actual number beside it.
- [ ] Exactly one variable changed, named.
- [ ] Manifest linked; tuple (prompt, model, dataset, grader, config) listed with versions.
- [ ] Baseline run on the same items, same day.
- [ ] Every gated metric in the results table, each with n and CI, plus cost and p95.
- [ ] At least one slice or trace example where the change hurt.
- [ ] Threats to validity addressed (contamination, judge bias, n, multiple comparisons).
- [ ] Explicit decision: promote / iterate / discard, and the next single experiment.
- [ ] Calibration note logged.

## Must not

- Claim a delta inside its CI as an improvement.
- Use "significantly" without a test or CI.
- Show only the aggregate.
- Mix dev and golden results in one table without labels.
- Exceed two pages before the appendix.

## Style

Numbers over adjectives. Active voice. Contractions fine. No em dashes. Tables for results, prose for interpretation.
