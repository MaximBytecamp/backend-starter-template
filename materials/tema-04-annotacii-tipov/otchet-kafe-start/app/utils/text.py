def _squash_spaces(value: str) -> str:
    return " ".join(value.split())


def normalize_name(name: str) -> str:
    return _squash_spaces(name).title()
