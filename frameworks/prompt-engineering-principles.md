# Prompt Engineering Principles

What reliably works, roughly in order of impact. Measure every change (`/prompt-iterate`); intuition about prompts is wrong more often than it feels.

## Structure

1. **Put the stable stuff in the system prompt, the variable stuff in the user turn.** Cache-friendly and easier to version.
2. **Be explicit about the output format.** Show the schema or a filled example. Ask for JSON only when you'll parse it; ask for a specific markdown structure otherwise.
3. **Delimit and label context.** Wrap retrieved documents and tool results in clear tags with ids. Tell the model these are data, not instructions (injection defense starts here).
4. **State the refusal path.** "If the documents don't contain the answer, say so and stop." Without this, the model fills the gap.
5. **Order matters.** Instructions, then context, then the question, then the format reminder. Long context: most important material at the start and end.

## Content

6. **Few-shot beats description for format and style.** 2–5 examples, diverse, including one edge case. Too many examples and the model copies surface features.
7. **Give the model room to think when the task needs it.** Ask for reasoning before the answer for multi-step problems; skip it for simple classification where it adds latency and can hurt.
8. **Positive instructions over prohibitions.** "Answer in one sentence" beats "Don't be verbose." Keep prohibitions for hard safety lines.
9. **Name the audience and the stakes.** "You're writing for an on-call engineer at 3am" changes output more than a paragraph of style rules.
10. **Ask for uncertainty explicitly.** "Rate your confidence and say what would change your answer."

## Robustness

11. **One change at a time, measured on the dev set, confirmed on golden.**
12. **Test with adversarial and off-distribution inputs.** Empty input, huge input, wrong language, instructions inside the data.
13. **Pin the model snapshot.** Prompts are tuned to a model; a silent model update is a change.
14. **Temperature 0 for anything evaluated or parsed.** Sample only for creative tasks, and then eval with repeated runs.
15. **Version and hash the prompt.** It's code. `prompts/<name>.md` with a change log, tests in the registry (`scaffolds/prompt-registry/`).

## Anti-patterns

- Stacking rules to patch each failure until the prompt is 3,000 tokens of contradictions. Refactor; move rules into examples or into code checks.
- "Be accurate." "Don't hallucinate." These do nothing measurable. Give the model the source and the refusal path instead.
- Tuning against the golden set.
- Judging by reading three outputs.
