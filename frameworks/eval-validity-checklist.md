# Eval Validity Checklist

Run this before trusting any eval result. Used by `/eval-review` and the `eval-skeptic` persona.

## Construct validity: does it measure what we care about?

- [ ] The metric maps to a user- or business-visible outcome. Name the mapping.
- [ ] The dataset covers the real input distribution (check slices: language, length, difficulty, segment, time).
- [ ] Edge cases from `failure-modes.md` are represented.
- [ ] The grader would fail an output that a user would reject, and pass one they'd accept. Spot-check 20.

## Contamination

- [ ] Items are not in any public benchmark the model may have trained on (search a few verbatim).
- [ ] Items are not in the fine-tuning data (hash overlap, near-dup check).
- [ ] Items were not used to iterate the prompt (dev/golden separation respected).
- [ ] For retrieval systems: gold documents are not trivially leaked by the query wording.

## Judge quality (LLM-as-judge)

- [ ] Rubric written, versioned, hashed in the manifest.
- [ ] Judge model fixed by snapshot; temperature 0.
- [ ] Calibrated against human labels: agreement reported (κ or %), n >= 100.
- [ ] Position bias: pairwise judgments swapped and averaged.
- [ ] Length bias: checked whether longer answers score higher independent of quality.
- [ ] Self-preference: judge is not the same model family as the system under test, or the bias is measured.
- [ ] Judge sees the reference / rubric, not the model identity.

## Statistics

- [ ] n reported; CI reported (bootstrap or Wilson for proportions).
- [ ] Comparison is paired on the same items when possible.
- [ ] Delta claimed is larger than the CI on the delta.
- [ ] Multiple comparisons: if k metrics or k variants were checked, correction applied or clearly labelled exploratory (`/stats-multiple-comparisons`).
- [ ] Non-determinism: run repeated at least 3× at the chosen temperature, or temperature 0 with seed.

## Operational

- [ ] Cost and latency measured on the same run.
- [ ] Results reproducible from the manifest alone by someone else.
- [ ] Golden set is frozen (hash) and gated thresholds are written down.

## Verdict

Pass / pass with caveats (list) / fail (which section). A failed validity check means the number is not evidence yet.
