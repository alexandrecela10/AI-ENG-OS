---
name: causal-dag
description: Draw the causal DAG for a question: treatment, outcome, confounders, mediators, colliders, selection; derive the adjustment set and the variables that must not be adjusted. Causal pack.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/causal-dag outputs/causal/summariser-ttr-question.md
/causal-dag --edges "usage->churn, tenure->usage, tenure->churn, plan->usage, plan->churn"
```

**What you get:** `outputs/causal/[slug]-dag.md`: edge list and a Mermaid diagram, node roles (confounder / mediator / collider / instrument candidate / selection), back-door paths, the minimal adjustment set(s), the do-not-adjust list, and the assumptions the DAG encodes that a skeptic would challenge.

**Time:** 30 minutes.

---

# /causal-dag

## Steps

1. Nodes: treatment, outcome, everything that plausibly causes either, how units entered the sample.
2. Edges with a one-line reason each. Unsure → draw it and flag it; an omitted edge is a strong claim.
3. Classify: confounders (cause both), mediators (X → M → Y), colliders (caused by two others), instruments (cause X only), selection nodes.
4. Back-door paths from X to Y; minimal adjustment set(s) that block them.
5. Do-not-adjust: mediators (unless direct effect wanted), colliders, descendants of X.
6. Unmeasured confounders: name them; they drive the sensitivity analysis.
7. Mermaid: `graph LR; tenure-->usage; tenure-->churn; usage-->churn`.

## Rules

- Every edge has a reason; every missing edge between plausibly related nodes is stated as an assumption.
- Run `causal-skeptic.md` on the DAG before estimating.
