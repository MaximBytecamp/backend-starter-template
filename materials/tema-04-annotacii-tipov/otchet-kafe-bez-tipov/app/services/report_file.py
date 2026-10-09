from pathlib import Path


def save_report(path, lines):
    with open(path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))
    return len(lines)
