from dataclasses import dataclass

from app.utils.text import normalize_name


@dataclass(frozen=True)
class Order:
    waiter: str
    kopeks: int

    def __post_init__(self):
        if self.kopeks < 0:
            raise ValueError("Сумма заказа не может быть отрицательной")
        object.__setattr__(self, "waiter", normalize_name(self.waiter))
