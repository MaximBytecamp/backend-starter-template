from datetime import date


def today_label() -> str:
    return date.today().strftime("%d.%m.%Y")
