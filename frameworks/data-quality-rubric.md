# Data Quality Rubric

Score each dimension 1–5. Anything at 2 or below blocks use for training or gated evals until fixed. Used by `/data-quality-audit` and `/dataset-card`.

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| **Provenance** | unknown source, no licence | source known, licence unclear | source, licence, collection window and consent documented |
| **Representativeness** | convenience sample | roughly matches production on 1–2 axes | stratified to match production on all key slices; gaps named |
| **Label quality** | single labeller, no guidelines | guidelines exist, agreement unmeasured | written guidelines, double-labelled sample, κ >= 0.7 reported |
| **Leakage** | splits random with no checks | exact-dup check only | exact + near-dup + temporal + group checks; overlap with eval golden sets verified zero |
| **Noise and duplicates** | unknown | dedupe done, noise unmeasured | dedupe done, label noise estimated on a sample, filtered |
| **PII / sensitive** | not checked | regex pass | detection + removal verified on a sample; retention policy set |
| **Documentation** | none | README | full dataset card with change log and hash |
| **Freshness** | age unknown | dated | dated, refresh policy, drift vs production measured |

## Quick checks to run every time

- Row count in → out at each filter step (a 90% drop is a finding).
- Class / slice balance vs production.
- 50 random rows read by a human. Write down what you saw.
- Exact and near-duplicate rate (MinHash or embedding cosine > 0.95).
- Overlap with every golden set in `context-library/evals/`.
- Longest and shortest 1%: are they garbage?
- Label distribution by labeller / by date (drift in labelling standards).

## Synthetic data extras

- Generator model and prompt versioned in the card.
- Diversity: distinct n-gram ratio, embedding spread, no template collapse.
- Filtered by a verifier that isn't the generator.
- Never eval on synthetic data from the same generator family as the system under test without saying so.
