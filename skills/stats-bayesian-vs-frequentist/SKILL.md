---
name: stats-bayesian-vs-frequentist
description: Decide whether a question is better answered with a Bayesian posterior (probability B beats A by at least X, expected loss) or a frequentist CI/test, set a defensible prior, and report both when useful. Stats pack.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/stats-bayesian-vs-frequentist "should we ship v5 given 412 paired items, +0.10 delta?"
/stats-bayesian-vs-frequentist --posterior --prior weak            → compute P(delta > 0), P(delta > MDE), expected loss
```

**What you get:** inline or `outputs/stats/bayes-[slug].md`: the recommendation (which framing and why), the prior with justification, the posterior summaries (P(B > A), P(B > A + MDE), expected loss of each decision) alongside the CI, and the sentence for the writeup that doesn't mix the two.

**Time:** 15 minutes.

---

# /stats-bayesian-vs-frequentist

## When Bayesian helps

- The decision needs a probability ("how likely is v5 at least 3 pts better?").
- Sequential decisions with small n per step (prompt iteration loops).
- Prior information is real (many past experiments of the same change type with known effect distribution, from the learning log).
- Expected-loss framing matches the business (cost of shipping a worse version vs cost of waiting).

## When frequentist is enough

- A single pre-registered comparison with adequate n and a gated floor.
- Regulatory or convention requires it.
- No defensible prior.

## Steps

1. Frame the decision; pick the framing.
2. Prior: weakly informative by default; informative only from the learning log with the data shown. State it.
3. Posterior for paired binary: Beta-Binomial on discordant pairs or a simple simulation; for continuous: normal approximation or bootstrap posterior.
4. Report: P(Δ > 0), P(Δ > MDE), expected loss per decision, and the frequentist CI beside it.
5. Sensitivity to the prior.

## Rules

- State the prior every time.
- Don't put a posterior probability and a p-value in one sentence without labelling them.
- Bayesian framing doesn't excuse peeking without a pre-specified decision rule.
