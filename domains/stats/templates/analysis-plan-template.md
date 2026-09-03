# Statistical Analysis Plan: [study]

**Owner:** [ ] · **Frozen on:** [date, hash] · **Reviewers:** statistician, [name]

## Question and decision

What we're estimating and what we'll do at each outcome.

## Primary outcome and metric

Definition, unit of analysis, how it's aggregated.

## Guardrails and secondary outcomes

Listed and capped. Anything not here is exploratory.

## Design

Paired / independent / clustered; randomisation or assignment; duration or n from `power-analysis-template.md`.

## Analysis

Estimator, test, CI method (bootstrap iterations, seed), handling of clustering, transformation (e.g. log latency), missing data rule, outlier rule (pre-specified).

## Multiple comparisons

Number of primary tests; correction method or hierarchical testing; exploratory labelling.

## Stopping rule

Fixed n / fixed duration / sequential method with parameters. No peeking otherwise.

## Subgroups

Pre-specified list with directional hypotheses. Others exploratory.

## Reporting

Per `{ai-eng-os}/domains/stats/frameworks/uncertainty-reporting.md`. Deviations from this plan logged in the writeup.
