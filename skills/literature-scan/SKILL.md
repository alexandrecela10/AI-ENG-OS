---
name: literature-scan
description: Quick, structured scan of prior work (papers, blog posts, open-source repos, internal docs) on a technique or problem, ending in a recommendation of what to try first and what to skip.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/literature-scan "reranking for RAG on short technical docs"
/literature-scan --internal-only          → only context-library/ and past experiments
/literature-scan --depth deep             → 15+ sources, includes replication notes
```

**What you get:** `outputs/reports/lit-scan-[slug]-[date].md`: question, what's known (with sources and dates), what's contested, what applies to our setting, ranked list of things to try with expected effect and cost, things to skip and why.

**Time:** 30–90 minutes depending on depth.

---

# /literature-scan

## Method

1. **State the question** as "for [our task/setting], does [technique] improve [metric] and at what cost?"
2. **Internal first.** `context-library/experiments/`, `decisions/`, `design-docs/`, the learning log. We may have tried it.
3. **External.** Prefer, in order: papers with released code and evals on tasks like ours; model provider docs and cookbooks; well-run public benchmarks; practitioner writeups with numbers. Skip anything without numbers.
4. **For each source** record: setting, claim with effect size, what would make it not transfer to us, date.
5. **Transfer judgement.** Our data size, model, latency budget, domain. Say what probably transfers and what probably doesn't.
6. **Recommend** at most three things to try, each as a one-variable experiment with a predicted effect, plus what to skip.

## Report

Use `{ai-eng-os}/voice/writing-style-research.md`. Sources as a table (source, year, setting, claim, effect, transfer risk). End with the experiment list ready for `/eval-spec`.

## Rules

- Dates on everything; this field moves fast and a 2023 result may be moot.
- Effect sizes, not adjectives.
- If you can't find numbers, say the evidence is anecdotal.
- No invented citations. If unsure a source exists, say so and describe what you'd look for.
