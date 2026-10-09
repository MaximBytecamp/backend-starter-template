def _squash_spaces(value):
    return " ".join(value.split())


def normalize_name(name):
    return _squash_spaces(name).title()
