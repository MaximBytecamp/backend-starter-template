from pathlib import Path

from app.domain.order import Order
from app.services.importer import read_rows


def load_orders(path: Path) -> list[Order]:
    return [
        Order(waiter=row["waiter"], kopeks=int(row["kopeks"]))
        for row in read_rows(path)
    ]


def revenue_by_waiter(orders: list[Order], top: int = 0) -> dict[str, int]:
    if not orders:
        raise ValueError("Список заказов пуст")
    totals: dict[str, int] = {}
    for order in orders:
        totals[order.waiter] = totals.get(order.waiter, 0) + order.kopeks
    ranked = sorted(totals.items(), key=lambda pair: -pair[1])
    if top:
        ranked = ranked[:top]
    return dict(ranked)


def sort_orders_in_place(orders: list[Order]) -> None:
    orders.sort(key=lambda order: -order.kopeks)
