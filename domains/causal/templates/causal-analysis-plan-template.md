# Causal Analysis Plan: [question]

**Owner:** [ ] · **Date (pre-registered):** [ ] · **Reviewers:** [causal-skeptic, statistician, name] · **Status:** Draft / Frozen

## Question

Business question: [ ]
Causal question: "What is the effect of [treatment X, defined as] on [outcome Y, defined as, measured when] for [population], compared to [control condition]?"
Estimand: ATE / ATT / LATE / CATE. Why this one: [ ].

## DAG

[diagram or edge list]. Confounders: [ ]. Mediators (not adjusted): [ ]. Colliders (not adjusted): [ ]. Adjustment set: [ ].

## Identification strategy

[strategy] because [data situation]. Key assumption in plain words: "[ ]". Most plausible violation: [ ]. What we'd see if it were violated: [ ].

## Data

Source, unit, period, treatment measurement, outcome measurement, covariates, exclusions. Sample size available: [ ]. Power for the smallest effect worth acting on ([ ]): [ ] (`/stats-power`).

## Analysis

Estimator and implementation. Standard errors (clustered at [ ]). Primary outcome: [ ]. Guardrails: [ ]. Pre-specified subgroups: [ ]. Stopping rule / duration: [ ].

## Assumption checks (to run and report)

From `{ai-eng-os}/domains/causal/frameworks/assumption-checks.md` for this strategy: [list].

## Sensitivity analyses

[e.g. E-value; alternative adjustment sets; alternative bandwidths; placebo tests]

## Decision rule

We will [action] if the effect on [Y] is [direction] with the CI excluding [threshold]; otherwise [ ].
