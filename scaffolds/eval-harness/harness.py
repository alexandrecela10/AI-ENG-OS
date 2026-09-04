"""Minimal eval runner. Replace call_model() with the project's client. Keep temperature 0 and a pinned snapshot."""
import argparse
import hashlib
import json
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from graders import ExactMatch, JsonSchemaGrader, LlmJudge
from stats import bootstrap_mean_ci, wilson

PRICE_PER_1K_TOKENS = {"input": 0.003, "output": 0.015}  # set per model


def call_model(system: str, user: str, model: str) -> tuple[str, dict]:
    """Return (text, usage) where usage = {"input_tokens": int, "output_tokens": int}. REPLACE ME."""
    raise NotImplementedError("wire this to the project's model client")


def sha256(path: str) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_jsonl(path: str) -> list[dict]:
    return [json.loads(line) for line in Path(path).read_text().splitlines() if line.strip()]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", required=True)
    ap.add_argument("--prompt", required=True, help="system prompt file")
    ap.add_argument("--model", required=True)
    ap.add_argument("--grader", choices=["exact", "json_schema", "llm_judge"], default="exact")
    ap.add_argument("--rubric", help="rubric path for llm_judge")
    ap.add_argument("--judge-model")
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int)
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    items = load_jsonl(args.dataset)[: args.limit]
    system = Path(args.prompt).read_text()

    if args.grader == "exact":
        grader = ExactMatch()
    elif args.grader == "json_schema":
        grader = JsonSchemaGrader()
    else:
        judge_model = args.judge_model or args.model
        grader = LlmJudge(args.rubric, lambda s, u: call_model(s, u, judge_model)[0])

    results, scores, latencies, cost = [], [], [], 0.0
    by_slice: dict[str, list[float]] = defaultdict(list)
    for item in items:
        t0 = time.perf_counter()
        text, usage = call_model(system, json.dumps(item["input"], ensure_ascii=False), args.model)
        ms = (time.perf_counter() - t0) * 1000
        g = grader.grade(item, text)
        cost += usage["input_tokens"] / 1000 * PRICE_PER_1K_TOKENS["input"] + usage["output_tokens"] / 1000 * PRICE_PER_1K_TOKENS["output"]
        score = float(g.passed)
        scores.append(score)
        latencies.append(ms)
        for k, v in item.get("slice", {}).items():
            by_slice[f"{k}={v}"].append(score)
        results.append({"id": item["id"], "output": text, "passed": g.passed, "score": g.score, "reason": g.reason, "latency_ms": round(ms), "usage": usage})

    n = len(scores)
    passed = int(sum(scores))
    lat = sorted(latencies)
    summary = {
        "n": n,
        "pass_rate": passed / n if n else 0,
        "ci95": wilson(passed, n),
        "per_slice": {k: {"n": len(v), "pass_rate": sum(v) / len(v), "ci95": bootstrap_mean_ci(v)} for k, v in sorted(by_slice.items())},
        "cost_usd_per_1k": cost / n * 1000 if n else 0,
        "latency_ms": {"p50": round(lat[n // 2]) if n else 0, "p95": round(lat[int(n * 0.95) - 1]) if n else 0},
    }
    manifest = {
        "id": out.name,
        "hypothesis": "FILL",
        "change": {"type": "FILL", "description": "FILL", "diff_ref": "FILL"},
        "tuple": {
            "prompt": {"path": args.prompt, "sha256": sha256(args.prompt)},
            "model": {"name": args.model},
            "dataset": {"path": args.dataset, "n": n, "sha256": sha256(args.dataset)},
            "grader": {"type": args.grader, "rubric": args.rubric, "rubric_sha256": sha256(args.rubric) if args.rubric else None},
            "config": {"temperature": 0},
        },
        "baseline": {"run_id": "FILL", "metrics": {}},
        "results": {"metrics": {"pass_rate": {"value": summary["pass_rate"], "ci95": summary["ci95"], "n": n}}, **{k: summary[k] for k in ("cost_usd_per_1k", "latency_ms")}},
        "decision": "FILL: promote | iterate | discard",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    (out / "results.jsonl").write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in results))
    (out / "summary.json").write_text(json.dumps(summary, indent=2))
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
