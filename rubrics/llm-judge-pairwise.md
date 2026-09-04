# Rubric: Pairwise Preference

**Version:** v1 · **Use for:** "is B better than A" on open-ended outputs. Always run each pair twice with positions swapped; a pair counts only if both orderings agree, otherwise it's a tie.

## Judge prompt

```
You will see a TASK and two responses, RESPONSE_1 and RESPONSE_2. Decide which better accomplishes the TASK for the intended user.

Criteria, in priority order: (1) correctness and faithfulness to any provided context, (2) completeness against the task, (3) clarity and appropriate length (shorter is better when content is equal), (4) adherence to requested format.

Ignore: which response is longer, confident tone, position.

Return JSON: {"winner":"1|2|tie","margin":"strong|slight","reason":"one sentence naming the criterion that decided it"}
```

## Aggregation

Win rate of B over A with a 95% CI (Wilson), tie rate, and the swap-consistency rate (how often the two orderings agreed). Consistency below 80% means the judge isn't reliable for this task.
