def format_kopeks(kopeks: int) -> str:
    return f"{kopeks / 100:,.2f} ₽".replace(",", " ").replace(".", ",")


def format_title(text: str, width: int = 40) -> str:
    return text.center(width, "=")
