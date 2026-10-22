import os

from app.utils.formatter import format_title
from app.utils.text import _squash_spaces


def total(prices):
    return sum(prices)


def pick(flag: bool) -> str:
    if flag:
        label = "есть выручка"
    return label


heading = format_title(40)
clean = _squash_spaces("иванов   пётр")
print(undefined_name)
