# Uncertainty Reporting

A number without its uncertainty is a rumour. Standard for every table in the OS.

## Every metric

`value [CI95 lower, upper], n = ...` — e.g. `0.87 [0.84, 0.90], n = 1,200`.

## Every comparison

`Δ = +0.10 [+0.06, +0.14]` on the **difference**, computed paired when the items are the same. Verdict language:
- CI excludes 0 → "real" / "evidence of a change"
- CI includes 0 → "no evidence of a change" (not "no change", not "slight improvement")
- CI excludes the floor in the wrong direction → "regression"

## Words to avoid and their replacements

| Avoid | Use |
|---|---|
| "significant" (without a test) | "CI excludes 0" / "outside the noise" |
| "trending toward" | "no evidence at this n; would need n ≈ X to detect" |
| "slightly better" (inside CI) | "no evidence of a difference" |
| "p < 0.05" alone | effect size with CI, then p if you must |
| "proves" | "is consistent with" / "supports" |

## Sample size in the sentence

"Accuracy up 6 pts (CI 3–9) on 412 items" beats "accuracy improved significantly".

## For executives

Translate the CI: "up about 6 points, give or take 3" · "somewhere between a small and a large improvement; we'd need two more weeks to narrow it". Keep the caveat; drop the notation.

## Multiple numbers

If you're showing k metrics or k variants, say k, and either correct or label exploratory (`/stats-multiple-comparisons`).

## Bayesian alternative

When a decision needs "how likely is it that B beats A by at least X", report the posterior probability with the prior stated. Don't mix a Bayesian probability and a frequentist CI in one sentence without saying which is which.

## Plots

Error bars are CIs, labelled as such. Paired comparisons plotted as differences, not as two bars.
