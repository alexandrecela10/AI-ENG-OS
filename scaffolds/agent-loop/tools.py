import inspect
from dataclasses import dataclass
from typing import Any, Callable, get_type_hints

_PY_TO_JSON = {str: "string", int: "integer", float: "number", bool: "boolean", list: "array", dict: "object"}


@dataclass
class Tool:
    name: str
    description: str
    fn: Callable[..., Any]
    schema: dict[str, Any]
    read_only: bool


REGISTRY: dict[str, Tool] = {}


def tool(description: str, read_only: bool = True):
    """Register a function as a tool. Description is a prompt: say what it returns, when to use it, side effects."""

    def deco(fn: Callable[..., Any]) -> Callable[..., Any]:
        hints = get_type_hints(fn)
        sig = inspect.signature(fn)
        props, required = {}, []
        for p in sig.parameters.values():
            props[p.name] = {"type": _PY_TO_JSON.get(hints.get(p.name, str), "string")}
            if p.default is inspect._empty:
                required.append(p.name)
        REGISTRY[fn.__name__] = Tool(
            name=fn.__name__,
            description=description,
            fn=fn,
            schema={"name": fn.__name__, "description": description, "input_schema": {"type": "object", "properties": props, "required": required}},
            read_only=read_only,
        )
        return fn

    return deco


def schemas() -> list[dict[str, Any]]:
    return [t.schema for t in REGISTRY.values()]


def call(name: str, args: dict[str, Any]) -> Any:
    """Errors are returned as data so the model can recover."""
    t = REGISTRY.get(name)
    if not t:
        return {"error": "unknown_tool", "hint": f"available: {sorted(REGISTRY)}"}
    try:
        return t.fn(**args)
    except TypeError as e:
        return {"error": "bad_arguments", "hint": str(e), "schema": t.schema["input_schema"]}
    except Exception as e:  # noqa: BLE001 - surface to the model as data
        return {"error": type(e).__name__, "hint": str(e)[:300]}
