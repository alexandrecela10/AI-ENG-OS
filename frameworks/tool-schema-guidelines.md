# Tool Schema Guidelines

A tool schema is a prompt. The model reads the name, description and parameter docs to decide when and how to call it. Write them for the model.

## Naming

- Verb-noun, specific: `search_orders`, `get_customer_by_email`, not `query` or `helper`.
- One tool, one job. If the description needs "or", split it.
- Avoid near-duplicates. If two tools overlap, the model will pick wrong some fraction of the time; measure it.

## Description

- First sentence: what it does and returns. Second: when to use it and when not to. Third (optional): gotchas.
- State side effects plainly: "Sends the email immediately. Irreversible."
- Include units, formats, limits: "dates as ISO-8601", "returns at most 50 rows".

## Parameters

- Typed, required vs optional explicit, enums where the set is closed.
- Describe each parameter with an example value.
- Prefer structured params over a single free-text string.
- No parameters the model can't know (internal ids it hasn't seen). Provide a lookup tool instead.

## Results

- Return structured data, compact. Trim fields the model doesn't need.
- Errors as data: `{ "error": "not_found", "hint": "try search_customers first" }`. The model can recover from a hint; it can't recover from a stack trace.
- Include ids the model will need for follow-up calls.
- Truncate long results with an explicit marker and a way to page.

## Safety

- Mark tools as read-only or side-effecting in the registry. Side-effecting tools go through the human gate for anything irreversible.
- Never let tool results contain instructions the model will follow. Wrap them as data.
- Validate arguments server-side; the schema is a hint to the model, not a security boundary.

## Testing a schema

- Write 10 natural requests that should call the tool and 10 that shouldn't. Measure selection accuracy and argument correctness (`/eval-build` can scaffold this).
- Check what the model does on error results.
- Re-run when adding any new tool: selection accuracy on the old tools can drop.
