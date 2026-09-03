# Domain packs

Three sub-OSes that share the AI Engineering OS spine (experiment manifest, eval loop, writeup standard, review panel, voice, `context-library/` + `outputs/`). Each pack adds frameworks and templates here and skills in `{ai-eng-os}/skills/` with a prefix.

| Pack | Prefix | Question it answers | Reviewer persona |
|---|---|---|---|
| `ml/` | `/ml-*` | Can we predict Y from X well enough, without fooling ourselves? | `ml-reviewer` |
| `causal/` | `/causal-*` | Did X cause Y, and how much? | `causal-skeptic` |
| `stats/` | `/stats-*` | Is this number real, and how sure are we? | `statistician` |

Shared skills work across packs: `/experiment-writeup`, `/eval-review`, `/decision-doc`, `/ai-review-panel`, `/status-update`. Outputs go to `outputs/ml/`, `outputs/causal/`, `outputs/stats/` in the working repo (created by `/ai-init --domains ml,causal,stats`).

Splitting a pack into its own plugin later: move `domains/<pack>/` and `skills/<prefix>-*` to a new repo, declare `requiredPlugins: ["alexandrecela10/AI-ENG-OS"]`, keep skill names. Nothing else changes.
