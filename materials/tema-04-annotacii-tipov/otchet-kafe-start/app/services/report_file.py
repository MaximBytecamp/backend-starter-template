from pathlib import Path


def save_report(path: Path, lines: list[str]) -> int:
    with open(path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))
    return len(lines)
