def build_component(kind: str, params: dict, registry: dict):
    kind = (kind or "off").lower()
    cls = registry.get(kind)
    if not cls:
        raise ValueError(f"Unknown component kind '{kind}'. Options: {list(registry)}")
    return cls(**(params or {}))