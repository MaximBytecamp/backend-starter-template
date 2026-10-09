import csv
from collections.abc import Iterator
from pathlib import Path


def read_rows(path):
    with open(path, encoding="utf-8", newline="") as file:
        yield from csv.DictReader(file)
