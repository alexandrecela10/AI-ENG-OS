# AI Engineering OS

A Devin plugin (also works with Claude Code) that templates, structures, measures and reviews the work of an AI engineer: evals first, one variable per experiment, versioned prompts, agent scaffolds with hard caps, red-teaming, launch gates, and writeups with confidence intervals. Includes three domain packs: ML, causal inference, statistical inference.

Sibling of [PM OS](https://github.com/alexandrecela10/PM-OS). Same shape: a shared engine installed once, and an empty per-repo workspace (`context-library/` + `outputs/`) scaffolded into every project.

## Philosophy

A PM's unit of work is a decision expressed as a doc. An AI engineer's is an **experiment expressed as a diff plus an eval delta**. So everything here is organised around one loop:

```
frame → spec the eval → baseline → change one thing → run eval → review the numbers → write up → promote or discard
```

Seven rules, always on (`AGENTS.md`):

1. Eval before build.
2. One variable per experiment; every run has a manifest.
3. Prompt, dataset, grader, model and config are versioned and hashed together.
4. Every number comes with n, a CI, cost and latency.
5. Every inference is traced.
6. A named human signs off before deploy.
7. New failure modes become regression cases.

## What you get

| | Where | What |
|---|---|---|
| **57 skills** | `skills/` | Frame, eval, prompt & agent, data, safety, ship, communicate, plus `ml-*`, `causal-*`, `stats-*` |
| **4 runnable scaffolds** | `scaffolds/` | eval harness (graders, LLM judge, bootstrap CIs, manifest writer), prompt registry, agent loop with caps and human gate, data pipeline |
| **16 templates** | `templates/` | experiment manifest, eval spec, prompt spec, design doc, dataset/model card, red-team report, launch readiness, postmortem, writeup, RFC, decision, rollout |
| **12 frameworks** | `frameworks/` | eval taxonomy and validity, prompt engineering, agent patterns, tool schemas, RAG, data quality, cost/latency, safety, rollout, failure modes, experiment discipline |
| **5 rubrics** | `rubrics/` | LLM-judge prompts (faithfulness, task quality, pairwise), writeup standard, code review standard |
| **10 reviewer personas** | `agents/` | eval-skeptic, red-teamer, safety, infra, research-scientist, user-advocate, ops, statistician, causal-skeptic, ml-reviewer |
| **3 domain packs** | `domains/` | ML lifecycle + leakage + metrics; causal identification + pitfalls + checks; stats test selection + uncertainty + common errors |
| **Voice** | `voice/` | research, design doc, incident, exec registers |

## Quick start

### Devin Cloud

An admin adds the plugin at https://app.devin.ai/settings/marketplace:

```json
{ "requiredPlugins": ["alexandrecela10/AI-ENG-OS"] }
```

Then in any project repo:

```
/ai-eng-os:ai-init --domains ml,causal,stats
```

### Devin CLI / Desktop

```bash
devin plugins install alexandrecela10/AI-ENG-OS
```

### Claude Code

Clone this repo next to your project and reference it; `.claude/skills` and `.claude/agents` symlink to `skills/` and `agents/`. Or add it as a Claude Code plugin from the repo.

### First hour

1. `/ai-init` in your project repo. Fill `context-library/project-brief.md` (system, users, gated metrics, budgets) and `stakeholders.md`.
2. Drop existing evals, prompts, datasets, decisions and postmortems into `context-library/`.
3. `/eval-spec` for the thing you're about to change. Then `/eval-build`, `/baseline`.
4. `/prompt-iterate` (or `/agent-design`, `/rag-design`). One change. `/eval-run-report`. `/experiment-writeup`.

Full walkthrough: [`setup/first-session-checklist.md`](setup/first-session-checklist.md).

## Directory structure

```
ai-eng-os/
├── README.md
├── AGENTS.md                    # always-on rules (short, loaded in every session)
├── CLAUDE.md                    # full operating instructions
├── .devin-plugin/plugin.json    # plugin manifest (name: ai-eng-os)
│
│   ── shared engine ──
├── skills/                      # 57 skills (.claude/skills → here)
├── agents/                      # 10 reviewer personas (.claude/agents → here)
├── scaffolds/                   # eval-harness/ prompt-registry/ agent-loop/ data-pipeline/
├── templates/                   # blank templates incl. experiment-manifest.json
├── frameworks/  rubrics/  voice/
├── domains/                     # ml/ causal/ stats/ (frameworks + templates per pack)
├── setup/  advanced/            # guides
└── scripts/validate-plugin.mjs  # CI check
```

In each project repo, after `/ai-init`:

```
your-project/
├── context-library/             # what the skills read: brief, stakeholders, failure-modes,
│   └── evals/ prompts/ datasets/ experiments/ decisions/ incidents/ design-docs/ other/
└── outputs/                     # what the skills write: one folder per experiment with manifest.json,
    └── experiments/ evals/ prompts/ design-docs/ datasets/ red-team/ postmortems/ reports/
        decisions/ tickets/ status-updates/ weekly-reviews/ traces/ scaffolds/ [ml/ causal/ stats/]
```

Folders are empty (`.gitkeep`) until you use them. Nothing generated is ever written into the plugin or into `context-library/`; you promote finished work by hand.

## Domain packs

| Pack | Question | Skills | Persona |
|---|---|---|---|
| ML | Can we predict Y from X without fooling ourselves? | `/ml-problem-framing` `/ml-data-split-audit` `/ml-baseline` `/ml-training-plan` `/ml-ablation` `/ml-error-analysis` `/ml-monitoring-plan` | `ml-reviewer` |
| Causal | Did X cause Y, and how much? | `/causal-question` `/causal-dag` `/causal-identification` `/causal-estimate` `/causal-sensitivity` `/causal-writeup` | `causal-skeptic` |
| Stats | Is this number real? | `/stats-power` `/stats-test-select` `/stats-multiple-comparisons` `/stats-bayesian-vs-frequentist` `/stats-uncertainty-report` `/stats-result-check` | `statistician` |

All three share the experiment manifest, writeup standard, review panel and voice. See [`domains/README.md`](domains/README.md).

## Guides

- [`setup/installation-guide.md`](setup/installation-guide.md): cloud, CLI, Claude Code, offline
- [`setup/first-session-checklist.md`](setup/first-session-checklist.md): 40-minute verification walkthrough
- [`setup/environment-keys.md`](setup/environment-keys.md): model provider and tracing keys, what needs what
- [`advanced/eval-harness-guide.md`](advanced/eval-harness-guide.md): wiring the harness, writing graders, calibrating a judge
- [`advanced/prompt-testing-guide.md`](advanced/prompt-testing-guide.md): registry, regression gates, CI
- [`advanced/agent-loop-guide.md`](advanced/agent-loop-guide.md): tools, caps, gates, tracing

## Working with PM OS

Both plugins can be installed together. Handoffs: `/pm-os:impact-sizing` → `/eval-spec`; `/pm-os:prd-draft` → `/design-doc`; `/experiment-writeup` → `/pm-os:feature-results`; `/decision-doc` in either. They never write into each other's folders.

## Validation

```bash
node scripts/validate-plugin.mjs
```

Runs in CI on every PR. Checks the manifest, every skill's frontmatter, every persona's frontmatter, and that every `{ai-eng-os}/...` path referenced by a skill exists.

## License

MIT. Anthropic, Claude and other names belong to their owners; this repo collects publicly known best practices and makes no claim to any organisation's internal process.
