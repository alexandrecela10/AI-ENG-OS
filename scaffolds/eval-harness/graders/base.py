from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass
class GradeResult:
    score: float  # 0..1 for binary/normalised, or 1..5 for rubric (set `scale`)
    passed: bool
    scale: str = "binary"  # "binary" | "likert5"
    reason: str = ""
    details: dict[str, Any] = field(default_factory=dict)


class Grader(Protocol):
    name: str

    def grade(self, item: dict[str, Any], output: str) -> GradeResult: ...
