from datetime import date


def today_label():
    return date.today().strftime("%d.%m.%Y")
