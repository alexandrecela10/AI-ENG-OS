# Installation Guide

AI Engineering OS is a shared engine. Install it once; use it in every project repo. Nothing project-specific lives in the plugin.

## Option A: Devin Cloud (recommended for teams)

1. An org admin opens https://app.devin.ai/settings/marketplace.
2. Add the plugin to the required list:
   ```json
   { "requiredPlugins": ["alexandrecela10/AI-ENG-OS"] }
   ```
   Private repo is fine; Devin fetches it through the GitHub integration.
3. Start a session in any repo. Skills appear as `/ai-eng-os:<name>` (e.g. `/ai-eng-os:eval-spec`). `AGENTS.md` rules load automatically.
4. In the project repo: `/ai-eng-os:ai-init` (add `--domains ml,causal,stats` if you want the pack folders). Commit the result.

Pin a version by tagging the plugin repo and referencing the tag if your admin wants controlled upgrades. Plugins are in beta; check https://docs.devin.ai/product-guides/plugins for current syntax.

## Option B: Devin CLI / Desktop (local)

```bash
devin plugins install alexandrecela10/AI-ENG-OS
devin plugins list
devin plugins update ai-eng-os        # later
```

User-level: applies to every project you open. Org-level manifests from Option A do not reach the CLI; install locally or set the manifest at the account/enterprise level.

## Option C: Claude Code

Two ways.

**As a Claude Code plugin** (if your Claude Code version supports plugin repos): add this repo as a plugin source; skills and agents are discovered through `.claude/skills` and `.claude/agents`, which are symlinks to `skills/` and `agents/`.

**Side by side** (works everywhere):
```bash
cd ~/work
git clone https://github.com/alexandrecela10/AI-ENG-OS.git ai-eng-os
cd your-project
claude "Read ../ai-eng-os/CLAUDE.md. Treat ../ai-eng-os as {ai-eng-os}. Run /ai-init here."
```
Skills reference shared files as `{ai-eng-os}/...`; tell Claude once per session where that root is, or add one line to your project's `CLAUDE.md`:
```
{ai-eng-os} = ../ai-eng-os (AI Engineering OS plugin root, read-only)
```

## Option D: Fully offline / vendored

Copy the plugin into the project under `tools/ai-eng-os/` and set `{ai-eng-os}` to that path. You lose automatic updates; you gain a frozen version for audits.

## What `/ai-init` creates

Empty, tracked folders and three blank context files in the **project** repo. Never touches the plugin. Idempotent: run it again after upgrades to add any new folders.

```
context-library/  project-brief.md  stakeholders.md  failure-modes.md  README.md
                  evals/ prompts/ datasets/ experiments/ decisions/ incidents/ design-docs/ other/
outputs/          experiments/ evals/ prompts/ design-docs/ datasets/ red-team/ postmortems/ reports/
                  decisions/ tickets/ status-updates/ weekly-reviews/ traces/ scaffolds/ [ml/ causal/ stats/]
```

Do not add `outputs/` to `.gitignore`. Outputs are drafts reviewed in PRs. Large artefacts (weights, big datasets) go to object storage; the manifest records the URI.

## Model provider keys

The scaffolds (`scaffolds/eval-harness`, `agent-loop`, `prompt-registry`) leave `call_model()` as a stub you wire to your project's existing client. No key is needed to install the plugin or run most skills. See `environment-keys.md` for what needs what.

## Upgrading

Plugin: `devin plugins update ai-eng-os` (CLI) or bump the ref in the marketplace manifest (cloud). Project: re-run `/ai-init` to pick up new folders; scaffolds you copied into `outputs/scaffolds/` or `src/` are yours and are not overwritten.

## Verify

```bash
node scripts/validate-plugin.mjs      # in the plugin repo
```
Then follow `first-session-checklist.md`.
