import json
from pathlib import Path
from typing import Any, Callable

from .base import GradeResult

CallModel = Callable[[str, str], str]  # (system, user) -> text


class LlmJudge:
    """Rubric-based judge. Rubric file must contain a fenced block with the judge prompt
    (see {ai-eng-os}/rubrics/llm-judge-*.md). Judge model is fixed; temperature 0 is the caller's job.
    Calibrate against human labels before gating on this (/judge-calibrate).
    """

    name = "llm_judge"

    def __init__(self, rubric_path: str, call_model: CallModel, pass_threshold: int = 4):
        text = Path(rubric_path).read_text()
        self.prompt = text.split("```")[1].strip()
        self.call_model = call_model
        self.pass_threshold = pass_threshold
        self.rubric_path = rubric_path

    def grade(self, item: dict[str, Any], output: str) -> GradeResult:
        user = json.dumps({"TASK": item["input"], "REFERENCE_OR_CONTEXT": item.get("expected"), "RESPONSE": output}, ensure_ascii=False)
        raw = self.call_model(self.prompt, user)
        try:
            verdict = json.loads(raw[raw.find("{"): raw.rfind("}") + 1])
            score = int(verdict["score"])
        except (ValueError, KeyError, json.JSONDecodeError):
            return GradeResult(score=0, passed=False, scale="likert5", reason="judge output unparseable", details={"raw": raw})
        return GradeResult(score=score, passed=score >= self.pass_threshold, scale="likert5", reason=verdict.get("reason", ""), details=verdict)
