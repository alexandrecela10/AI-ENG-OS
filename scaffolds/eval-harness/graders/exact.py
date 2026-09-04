import re
from typing import Any

from .base import GradeResult


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())


class ExactMatch:
    name = "exact"

    def grade(self, item: dict[str, Any], output: str) -> GradeResult:
        expected = item["expected"]
        if isinstance(expected, list):
            ok = any(_norm(str(e)) == _norm(output) for e in expected)
        else:
            ok = _norm(str(expected)) == _norm(output)
        return GradeResult(score=1.0 if ok else 0.0, passed=ok, reason="" if ok else f"expected {expected!r}")
