# Red-Team Report: [system] round [n]

**Lead:** [name] · **Dates:** [ ] · **Target version:** [prompt/model/scaffold versions] · **Scope:** [what was in and out of bounds]

## Summary

Attacks tried: [n] across [k] categories. Successful: [n] ([%]). Severity split: [critical / high / medium / low]. Two most important findings in one sentence each.

## Method

- **Attackers:** [humans (n, background) / automated (model, prompt) / both]
- **Attack categories:** from `{ai-eng-os}/frameworks/safety-checklist.md` § attack taxonomy, plus [project-specific]
- **Success criterion:** [what counts as a break, who adjudicated]
- **Budget:** [attempts per category, time]

## Findings

| ID | Category | Attack (summary) | Result | Severity | Repro trace | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| RT-01 | prompt injection via retrieved doc | | broke | high | | | | open |

## Mitigations applied and re-test

| Mitigation | Finding(s) addressed | Re-test result | Eval delta on gated metrics |
|---|---|---|---|

## Residual risk

What's still open, likelihood, impact, and the argument for shipping anyway (or not).

## Added to regression

Golden-set cases added: [ids]. Failure modes appended: [ids].
