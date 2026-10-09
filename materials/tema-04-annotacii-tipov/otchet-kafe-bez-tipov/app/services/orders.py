from pathlib import Path

from app.domain.order import Order
from app.services.importer import read_rows


def load_orders(path):
    return [
        Order(waiter=row["waiter"], kopeks=int(row["kopeks"]))
        for row in read_rows(path)
    ]


def revenue_by_waiter(orders, top=0):
    if not orders:
        raise ValueError("Список заказов пуст")
    totals = {}
    for order in orders:
        totals[order.waiter] = totals.get(order.waiter, 0) + order.kopeks
    ranked = sorted(totals.items(), key=lambda pair: -pair[1])
    if top:
        ranked = ranked[:top]
    return dict(ranked)


def sort_orders_in_place(orders):
    orders.sort(key=lambda order: -order.kopeks)
