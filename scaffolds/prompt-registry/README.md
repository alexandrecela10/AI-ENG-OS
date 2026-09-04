# prompt-registry

Prompts are code. Each prompt is a markdown file with frontmatter, versioned in git, hashed at load time, and tested against the golden set.

```
prompt-registry/
├── prompts/
│   └── example.md        # frontmatter: name, version, model, eval, owner; body = the prompt
├── registry.py           # load(name) -> Prompt(text, version, sha256, meta); render(vars)
└── test_prompts.py       # runs the harness on every prompt's declared eval; fails if a gated metric drops
```

## Rules

- One change per version bump. Add a change-log line in the frontmatter with the manifest id.
- `model` in frontmatter is the snapshot the prompt was tuned on. Bumping it is a change.
- Never edit a promoted version in place; copy to `v+1`.
- The registry hash goes into every manifest and every trace.

## Pre-push hook (optional)

```bash
# .git/hooks/pre-push
python prompt-registry/test_prompts.py --changed-only || exit 1
```
