import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Callable

Row = dict
Step = Callable[[list[Row]], list[Row]]

PII_PATTERNS = {
    "email": re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"),
    "phone": re.compile(r"\+?\d[\d\s().-]{8,}\d"),
    "card": re.compile(r"\b(?:\d[ -]*?){13,16}\b"),
}


def text_of(row: Row) -> str:
    return json.dumps(row.get("input", row), ensure_ascii=False)


def drop_empty(rows: list[Row]) -> list[Row]:
    return [r for r in rows if text_of(r).strip() not in ("", "{}", "null")]


def drop_length_outliers(rows: list[Row], lo: int = 10, hi: int = 20_000) -> list[Row]:
    return [r for r in rows if lo <= len(text_of(r)) <= hi]


def exact_dedupe(rows: list[Row]) -> list[Row]:
    seen, out = set(), []
    for r in rows:
        k = text_of(r)
        if k not in seen:
            seen.add(k)
            out.append(r)
    return out


def _shingles(s: str, k: int = 5) -> set[str]:
    s = re.sub(r"\s+", " ", s.lower())
    return {s[i : i + k] for i in range(max(1, len(s) - k + 1))}


def near_dedupe(rows: list[Row], threshold: float = 0.9) -> list[Row]:
    kept: list[tuple[set[str], Row]] = []
    for r in rows:
        sh = _shingles(text_of(r))
        if any(len(sh & k) / max(1, len(sh | k)) >= threshold for k, _ in kept):
            continue
        kept.append((sh, r))
    return [r for _, r in kept]


def scrub_pii(rows: list[Row]) -> list[Row]:
    out = []
    for r in rows:
        s = json.dumps(r, ensure_ascii=False)
        for name, pat in PII_PATTERNS.items():
            s = pat.sub(f"<{name}>", s)
        out.append(json.loads(s))
    return out


STEPS: list[tuple[str, Step]] = [
    ("drop_empty", drop_empty),
    ("drop_length_outliers", drop_length_outliers),
    ("exact_dedupe", exact_dedupe),
    ("near_dedupe", near_dedupe),
    ("scrub_pii", scrub_pii),
]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--report", required=True)
    a = ap.parse_args()

    rows = [json.loads(l) for l in Path(a.inp).read_text().splitlines() if l.strip()]
    report = {"steps": [], "n_in": len(rows)}
    for name, fn in STEPS:
        before = len(rows)
        rows = fn(rows)
        report["steps"].append({"step": name, "in": before, "out": len(rows), "dropped_pct": round(100 * (before - len(rows)) / max(1, before), 2)})
    lengths = sorted(len(text_of(r)) for r in rows)
    report["n_out"] = len(rows)
    report["length_chars"] = {"p5": lengths[len(lengths) // 20] if lengths else 0, "p50": lengths[len(lengths) // 2] if lengths else 0, "p95": lengths[int(len(lengths) * 0.95) - 1] if lengths else 0}
    report["slice_counts"] = dict(Counter(json.dumps(r.get("slice", {}), sort_keys=True) for r in rows).most_common(20))
    Path(a.out).write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows))
    Path(a.report).write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
