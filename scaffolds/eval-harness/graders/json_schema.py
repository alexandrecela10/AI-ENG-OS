import json
from typing import Any

from .base import GradeResult


class JsonSchemaGrader:
    """Passes if output parses as JSON and has the expected keys with the expected types.

    `item["expected"]` is a dict of key -> python type name ("str", "int", "list", ...).
    Swap in `jsonschema` if the project already depends on it.
    """

    name = "json_schema"
    _types = {"str": str, "int": int, "float": (int, float), "bool": bool, "list": list, "dict": dict}

    def grade(self, item: dict[str, Any], output: str) -> GradeResult:
        try:
            obj = json.loads(output)
        except json.JSONDecodeError as e:
            return GradeResult(score=0.0, passed=False, reason=f"invalid json: {e.msg}")
        missing, wrong = [], []
        for key, tname in item["expected"].items():
            if key not in obj:
                missing.append(key)
            elif not isinstance(obj[key], self._types[tname]):
                wrong.append(key)
        ok = not missing and not wrong
        return GradeResult(score=1.0 if ok else 0.0, passed=ok, reason=f"missing={missing} wrong_type={wrong}" if not ok else "")
