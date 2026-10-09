from datetime import date

from app.domain.order import Order


class Shift:
    def __init__(self, day):
        self.day = day
        self.orders = []

    def add(self, order):
        self.orders.append(order)

    def total_kopeks(self):
        return sum(order.kopeks for order in self.orders)
