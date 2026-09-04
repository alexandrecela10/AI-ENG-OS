# Experiment Discipline

The loop every change follows. Skills enforce it; this explains why.

```
frame → spec the eval → baseline → change one thing → run → review numbers → write up → promote / iterate / discard
```

## Rules

1. **Hypothesis first, with a predicted number.** "v4 will raise refusal precision from 0.81 to at least 0.90." A prediction you can be wrong about is what makes it an experiment. Calibration over time is the payoff.
2. **One variable.** Prompt or model or data or decoding or scaffold. If you changed two, you learned nothing attributable. Interaction effects come later, deliberately, as their own experiments.
3. **Baseline on the same items, same grader, same day.** Providers drift; graders drift; datasets rotate. Re-run the baseline alongside the candidate.
4. **Manifest or it didn't happen.** `templates/experiment-manifest.json` filled completely, hashes included, in `outputs/experiments/<id>/`.
5. **Dev for iteration, golden for decisions.** Iterate freely on dev. Touch golden once per candidate you'd actually ship.
6. **Report the delta with its CI, on every gated metric, plus cost and latency.** A delta inside the noise is "no evidence", not "slight improvement".
7. **Look at the traces.** Numbers say whether; traces say why. Read 10 wins and 10 losses before writing the writeup.
8. **Write it up the same day.** `templates/experiment-writeup-template.md`. Discarded experiments get written up too; they're the ones people repeat.
9. **Decide explicitly.** promote / iterate / discard, with one sentence of rationale in the manifest.
10. **Log the calibration.** Predicted vs actual, by change type, in `context-library/ai-eng-os-learning-log.md`.

## Experiment sizes

| Size | When | Golden touch? | Writeup |
|---|---|---|---|
| Probe | 30-item dev sample to see if an idea is alive | no | one paragraph in the log |
| Dev run | full dev set | no | short writeup |
| Candidate | full dev + golden, cost + latency | yes, once | full writeup, review by `eval-skeptic` |
| Release | candidate + regression suite + safety suite | yes | writeup + launch readiness |

## Common ways experiments lie

Contaminated items · judge that prefers longer outputs · comparing runs on different item subsets · temperature > 0 with a single run · picking the best of k variants without correcting · dev/golden mixing · unpinned model · cherry-picked traces. `frameworks/eval-validity-checklist.md` catches most of these.
