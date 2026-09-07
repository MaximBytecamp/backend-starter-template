# Выдача книг в библиотеке. Один файл, как и сервис заказов на паре.
# Ваша задача на домашнее задание — разрезать его на пакет.

import json
import os
from datetime import date, datetime, timedelta

DATA_FILE = "loans.json"
FINE_PER_DAY = 5
FREE_DAYS = 14
LIMITS = {"student": 5, "teacher": 10}
LOANS = []


def load():
    global LOANS
    if not os.path.exists(DATA_FILE):
        LOANS = []
        return LOANS
    with open(DATA_FILE, encoding="utf-8") as f:
        LOANS = json.load(f)
    return LOANS


def save():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(LOANS, f, ensure_ascii=False, indent=2)


def find(loan_id):
    for l in LOANS:
        if l["id"] == loan_id:
            return l
    return None


def by_reader(card):
    out = []
    for l in LOANS:
        if l["card"] == card and l["returned_at"] is None:
            out.append(l)
    return out


def days_overdue(loan):
    started = datetime.fromisoformat(loan["taken_at"]).date()
    end = date.fromisoformat(loan["returned_at"]) if loan["returned_at"] else date.today()
    d = (end - started).days - FREE_DAYS
    if d < 0:
        d = 0
    return d


def fine(loan):
    f = FINE_PER_DAY
    if loan["role"] == "student":
        f = f / 2
    return f * days_overdue(loan)


def can_take(card, role):
    limit = LIMITS.get(role)
    if limit is None:
        print("неизвестная роль", role)
        return False
    return len(by_reader(card)) < limit


def take(card, role, book):
    if not can_take(card, role):
        print("лимит исчерпан")
        return None
    new_id = 1
    for l in LOANS:
        if l["id"] >= new_id:
            new_id = l["id"] + 1
    loan = {
        "id": new_id,
        "card": card,
        "role": role,
        "book": book,
        "taken_at": datetime.now().isoformat(),
        "returned_at": None,
    }
    LOANS.append(loan)
    save()
    return loan


def give_back(loan_id):
    l = find(loan_id)
    if l is None:
        print("нет такой выдачи")
        return
    if l["returned_at"] is not None:
        print("книга уже возвращена")
        return
    l["returned_at"] = date.today().isoformat()
    save()
    print("принято, штраф:", fine(l))


def debtors():
    load()
    print("ДОЛЖНИКИ")
    print("-" * 52)
    money = 0
    for l in LOANS:
        if l["returned_at"] is None and days_overdue(l) > 0:
            money = money + fine(l)
            print(str(l["id"]).rjust(3), l["card"].ljust(10), l["book"].ljust(24), str(fine(l)).rjust(6))
    print("-" * 52)
    print("всего штрафов:", money)


if __name__ == "__main__":
    debtors()
