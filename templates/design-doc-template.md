# [System / Change] Design Doc

**Owner:** [name] · **Reviewers:** [names] · **Status:** Draft / In review / Approved · **Last updated:** [date]

## 1. Problem and success metric

One paragraph: who has what problem, how we'll know it's solved. Name the eval (`evals/...`) and the gated metrics from `context-library/project-brief.md`.

## 2. Constraints

Cost ceiling, latency budget, data constraints, safety/policy constraints, dependencies. Constraints first so the design can be checked against them.

## 3. Proposed design

Diagram or numbered flow. For model-backed systems, be explicit about:
- Model(s), snapshots, decoding config
- Prompt structure (system / developer / user; where retrieved content goes; where tool results go)
- Tools and their schemas (`/tool-schema`)
- Retrieval: index, chunking, top-k, reranking (`/rag-design`)
- Loop control: max steps, budget guard, stop conditions, human gate
- Tracing: what's logged, where, retention

## 4. Alternatives considered

| Alternative | Why not (or why maybe later) |
|---|---|

## 5. Evaluation plan

Which eval, which baseline, what delta would justify shipping, what would make us stop. Link `/eval-spec` output.

## 6. Risks and failure modes

Pull from `context-library/failure-modes.md`; add new ones. For each: detection signal, mitigation, owner.

## 7. Rollout

Canary %, promotion criteria, rollback trigger, kill switch owner. Link `/rollout-plan`.

## 8. Open questions

- [ ] [question] — @[owner]
