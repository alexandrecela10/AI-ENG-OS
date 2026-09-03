# Eval Taxonomy

Four kinds of eval. Every system needs at least one of each before GA. Confusing them is the most common eval mistake.

| Kind | Question | Typical metric | Dataset | Who owns |
|---|---|---|---|---|
| **Capability** | Can the model do the task? | accuracy, F1, pass@k, exact match, BLEU-ish only when nothing better exists | representative sample of real inputs, stratified by difficulty | eng |
| **Behavior** | Does it do the task the way we want? | format compliance, citation rate, verbosity, tone rubric score, instruction-following | hand-built cases per behavior contract line | eng + product |
| **Safety** | Does it refuse what it should and only that? | refusal precision and recall, jailbreak success rate, harmful-content rate | adversarial + benign-lookalike pairs | safety |
| **Regression** | Did anything we already fixed break? | pass rate on frozen cases | one case per closed failure mode (`failure-modes.md`) | eng, grows forever |

## Levels of grading, cheapest first

1. **Deterministic code**: exact match, JSON schema check, unit tests on generated code, regex on citations. Use whenever the answer has a checkable form.
2. **Reference-based**: compare to a gold answer with a tolerant matcher (normalized string, set overlap, numeric tolerance).
3. **LLM judge with rubric**: for open-ended text. Requires a written rubric (`rubrics/`), a fixed judge model, and a calibration run against human labels (`/judge-calibrate`). Report agreement.
4. **Pairwise preference**: judge picks A vs B. Position-swap every pair. Good for "is v2 better than v1", bad for absolute tracking.
5. **Human**: gold standard, expensive. Use to calibrate 3 and 4 and for anything gated on safety.

## Splits

- **Golden**: frozen, gated, never iterated against. Rotate items only through an approved refresh.
- **Dev**: for iteration. Expect to overfit it a little; that's what golden is for.
- **Held-out slices**: by language, user segment, difficulty, input length. Report per-slice, not just aggregate.

## Sizing

Rule of thumb for a binary metric near 0.8: n = 400 gives a 95% CI of about ±4 pts; n = 1,000 gives ±2.5. For detecting a 3-pt delta between two runs on the same items, use paired analysis and expect to need n ≈ 500+. Run `/stats-power` rather than guessing.

## Metric hygiene

- Every number: n, CI, cost, latency. No exceptions.
- Paired comparisons (same items, two systems) beat unpaired.
- Report the slice where the change hurt, even if aggregate improved.
- "Cost per correct answer" often beats accuracy as the decision metric.
- Watch for Goodhart: when a metric becomes the target, add a second one that would catch gaming.
