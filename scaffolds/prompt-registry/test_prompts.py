"""Run each prompt's declared eval and fail if a gated metric is below its floor.
Wire `run_eval` to the eval-harness (or your tracing/eval platform)."""
import json
import sys

from registry import all_prompts


def run_eval(prompt_path: str, dataset: str, grader: str) -> dict:
    """Return the harness summary dict ({"pass_rate": .., "ci95": [..], "n": ..}). REPLACE ME."""
    raise NotImplementedError


def parse_gated(spec: str) -> dict[str, float]:
    """Frontmatter format: `gated_metrics: pass_rate=0.85, refusal_precision=0.90`."""
    return {k.strip(): float(v) for k, v in (pair.split("=") for pair in spec.split(",") if "=" in pair)}


def main() -> int:
    failures = []
    for p in all_prompts():
        gated = parse_gated(p.meta.get("gated_metrics", ""))
        if not gated:
            continue
        summary = run_eval(f"prompts/{p.name}.md", p.meta["eval"], p.meta.get("grader", "exact"))
        for metric, floor in gated.items():
            value = summary[metric]
            if value < float(floor):
                failures.append(f"{p.name}@{p.version}: {metric}={value:.3f} < floor {floor} (n={summary['n']}, ci95={summary['ci95']})")
    for f in failures:
        print("FAIL", f)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
