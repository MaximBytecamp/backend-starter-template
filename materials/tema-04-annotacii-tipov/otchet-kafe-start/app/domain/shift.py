from datetime import date

from app.domain.order import Order


class Shift:
    def __init__(self, day: date) -> None:
        self.day = day
        self.orders: list[Order] = []

    def add(self, order: Order) -> None:
        self.orders.append(order)

    def total_kopeks(self) -> int:
        return sum(order.kopeks for order in self.orders)
