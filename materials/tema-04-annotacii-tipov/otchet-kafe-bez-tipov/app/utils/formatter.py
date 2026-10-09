def format_kopeks(kopeks):
    return f"{kopeks / 100:,.2f} ₽".replace(",", " ").replace(".", ",")


def format_title(text, width=40):
    return text.center(width, "=")
