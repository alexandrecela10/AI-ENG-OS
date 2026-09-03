# Writing Style: Engineering Design Doc

**Audience:** reviewers who need to find the flaw before it ships.

- Constraints before design. Cost ceiling, latency budget, safety lines and data rules on page one so every later choice can be checked against them.
- Alternatives with real trade-offs, including "do nothing". If an alternative has no cons listed, you haven't thought about it.
- Edge cases explicit: empty input, huge input, tool failure, model refusal, budget exhaustion, provider outage.
- Diagrams over prose for flows; prose over diagrams for rationale.
- Name what you don't know as open questions with owners.
- Every claim about behavior points to an eval or says "unmeasured".
- Terse. A design doc is read three times and skimmed thirty.
- Contractions fine. No em dashes. No "robust", "scalable" or "leverage".
