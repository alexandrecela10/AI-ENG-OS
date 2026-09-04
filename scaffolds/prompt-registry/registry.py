import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

PROMPTS_DIR = Path(__file__).parent / "prompts"


@dataclass(frozen=True)
class Prompt:
    name: str
    version: str
    sha256: str
    meta: dict[str, Any]
    text: str

    def render(self, **vars: Any) -> str:
        missing = [v for v in re.findall(r"{{(\w+)}}", self.text) if v not in vars]
        if missing:
            raise KeyError(f"missing prompt variables: {missing}")
        out = self.text
        for k, v in vars.items():
            out = out.replace("{{" + k + "}}", str(v))
        return out


def _parse_frontmatter(raw: str) -> tuple[dict[str, Any], str]:
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m:
        raise ValueError("prompt file needs YAML frontmatter")
    meta: dict[str, Any] = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "-")):
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, m.group(2)


def load(name: str) -> Prompt:
    path = PROMPTS_DIR / f"{name}.md"
    raw = path.read_text()
    meta, text = _parse_frontmatter(raw)
    return Prompt(name=name, version=meta.get("version", "v0"), sha256=hashlib.sha256(raw.encode()).hexdigest(), meta=meta, text=text.strip())


def all_prompts() -> list[Prompt]:
    return [load(p.stem) for p in sorted(PROMPTS_DIR.glob("*.md"))]
