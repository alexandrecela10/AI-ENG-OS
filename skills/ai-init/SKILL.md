---
name: ai-init
description: Scaffold the AI Engineering OS workspace (context-library/ and outputs/ folders, blank project brief, stakeholders, failure-mode catalogue) in the current project repo so every other skill has somewhere to read from and write to.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

```
/ai-init                 → Scaffold context-library/ and outputs/ in the current repo
/ai-init --dry-run       → Show what would be created, create nothing
/ai-init --domains ml,causal,stats   → Also create domain-pack folders
```

**What you get:** the standard workspace, empty except for `.gitkeep` files and three blank context files. Idempotent: existing files are never overwritten.

**Time:** under a minute.

---

# /ai-init - Scaffold an AI Engineering OS workspace

AI Engineering OS is the shared engine (skills, templates, scaffolds, frameworks, personas). Each project repo owns its context and outputs. This skill creates that per-repo half.

## Steps

1. **Confirm the target.** The target is the root of the repo the user is working in (the folder containing `.git`). Never scaffold inside `{ai-eng-os}` itself unless the user is explicitly working on the OS as a product.

2. **Create the folders.** For each path below, create it if missing and add an empty `.gitkeep`:

   ```
   context-library/
   ├── evals/           # frozen golden sets, past eval results you trust
   ├── prompts/         # promoted prompt versions (the registry of record)
   ├── datasets/        # dataset cards + provenance notes
   ├── experiments/     # promoted experiment writeups
   ├── decisions/       # ADRs / decision docs
   ├── incidents/       # postmortems
   ├── design-docs/     # approved design docs
   └── other/
   outputs/
   ├── experiments/  evals/  prompts/  design-docs/  datasets/  red-team/
   ├── postmortems/  reports/  decisions/  tickets/  status-updates/
   ├── weekly-reviews/  scaffolds/  traces/
   └── (with --domains) ml/  causal/  stats/
   ```

3. **Copy the blank context files** into `context-library/` under the names every skill looks for. Skip any that already exist:

   | From | To |
   |------|----|
   | `{ai-eng-os}/templates/project-brief-template.md` | `context-library/project-brief.md` |
   | `{ai-eng-os}/templates/stakeholders-template.md` | `context-library/stakeholders.md` |
   | `{ai-eng-os}/templates/failure-modes-template.md` | `context-library/failure-modes.md` |

4. **Write `context-library/README.md`** (skip if present): what goes in each folder, that skills read from here and write to `outputs/`, and that `project-brief.md` must be filled first.

5. **Report.** List created and skipped paths. Then suggest:
   - Fill in `context-library/project-brief.md`: what the system does, users, gated metrics, cost and latency budgets.
   - Run `/eval-spec` on the thing you're about to change, or `/problem-framing` if it's new.

## Rules

- Never overwrite an existing file. Print "exists, skipped".
- Do not add `outputs/` to `.gitignore`. Outputs are drafts reviewed in PRs. Large artifacts (model weights, big datasets) belong in object storage; the manifest records the URI.
- If the repo already has part of the structure, only fill the gaps.
- With `--dry-run`, print the plan as a tree and stop.

## Example

```
/ai-init --domains stats

Scaffolding AI Engineering OS workspace in agentic_product_analyst/

Created:
  context-library/{evals,prompts,datasets,experiments,decisions,incidents,design-docs,other}/.gitkeep
  context-library/project-brief.md
  context-library/stakeholders.md
  context-library/failure-modes.md
  context-library/README.md
  outputs/{experiments,evals,prompts,...,stats}/.gitkeep

Skipped (already present):
  none

Next: fill in context-library/project-brief.md, then run /eval-spec.
```
