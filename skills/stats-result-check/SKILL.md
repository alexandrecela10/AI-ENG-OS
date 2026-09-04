---
name: stats-result-check
description: "Is this result real?" Fast statistical review of any claim or table using the common-errors list and the statistician persona: unit, pairing, n, CI, multiplicity, peeking, non-determinism. Verdict plus the fix. Stats pack.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/stats-result-check outputs/experiments/2026-09-03-v5/report.md
/stats-result-check "accuracy went from 0.84 to 0.88 on 50 examples, ship it"
```

**What you get:** inline (or `outputs/stats/result-check-[slug].md`): verdict (sound / sound with caveats / not sound), the errors found from `{ai-eng-os}/domains/stats/frameworks/common-statistical-errors.md` with the fix for each, the honest CI where computable, and the smallest change to the analysis or design that would make the result trustworthy.

**Time:** 5–10 minutes.

---

# /stats-result-check

Adopt `{ai-eng-os}/agents/statistician.md`.

## Triage questions

Unit of analysis? Paired or independent, and analysed as such? n per arm and per slice? CI on the difference? How many metrics, slices, variants, looks? Effect size fixed before the data? Repeats for non-deterministic runs? Ordinal treated as interval? Heavy tails?

## Output

```
Claim: v5 beats v4 by 4 pts (0.84 → 0.88) on 50 items.
Check: paired? unknown. n = 50 → CI on an unpaired delta ≈ ±14 pts; even paired with 20% disagreement ≈ ±9 pts. Verdict: not sound as evidence.
Honest statement: "no evidence of a difference at n = 50; detectable effect ≈ 9–14 pts."
Smallest fix: run both on the 412-item golden set paired (expected CI ≈ ±3 pts).
```

## Rules

- Specific numbers, not "sample may be small".
- Sound with caveats means the caveats go in the writeup's TL;DR.
- Hand deep issues to `/stats-test-select`, `/stats-power`, `/stats-multiple-comparisons`.
