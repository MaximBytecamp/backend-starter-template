# Тема 4 · Аннотации типов

**Глава 4.1:** https://algorthimization-course-vvodnoe.vercel.app/mdk0101-razrabotka-modulei/lessons/04-docstrings-i-dokumentaciya/01-annotacii-tipov.html

**Глава 4.2:** https://algorthimization-course-vvodnoe.vercel.app/mdk0101-razrabotka-modulei/lessons/04-docstrings-i-dokumentaciya/02-tipy-v-annotaciyah.html

**Файлы занятия:** [materials/tema-04-annotacii-tipov](../materials/tema-04-annotacii-tipov/) —
проект «Отчёт кафе» с аннотациями и без них.

## Содержание лекции

На занятиях пройдены главы 4.1 и 4.2 книги темы.

### 4.1 Что такое аннотация типа

**Аннотация типа** — запись в коде, которая сообщает, значение какого типа
ожидается в параметре, переменной или результате функции.

```python
def shorten(text: str, width: int = 40) -> str:
    ...

totals: dict[str, int] = {}
```

| Где | Запись |
|---|---|
| параметр | `text: str`, со значением по умолчанию — `width: int = 40` |
| результат | `-> str`; функция ничего не возвращает — `-> None` |
| переменная, атрибут | `totals: dict[str, int] = {}`, `self.orders: list[Order] = []` |
| метод | `def add(self, order: Order) -> None`; `self` не аннотируют |

При запуске Python аннотации не проверяет: он сохраняет их
в `__annotations__`. Пользу дают редактор и инструменты: подсказка
по наведению (Ctrl+K, Ctrl+I) и автодополнение (Ctrl+Пробел) знают тип
значения.

### 4.2 Типы в аннотациях

| Что | Запись |
|---|---|
| простые типы | `int`, `float`, `str`, `bool`, `None` |
| коллекции | `list[int]`, `dict[str, int]`, `tuple[int, int]`, `tuple[int, ...]`, `set[str]` |
| собственный класс | `Order` |
| значение или None | `Order \| None`; перед работой проверяют `if x is not None:` |
| несколько типов | `int \| str` |
| функция-аргумент | `Callable[[Order], int]` из `collections.abc` |
| итератор | `Iterator[dict[str, str]]` |
| псевдоним | `type Kopeks = int` — для проверки это тот же `int` |
| любой тип | `Any` — проверка для значения выключена |

## Что делали на занятии

1. Разобрали подписи функций проекта «Отчёт кафе» и подсказки редактора
   по наведению.
2. Разобрали записи типов: коллекции, значение или `None`, несколько типов,
   функции-аргументы, псевдонимы.

## Что вошло в проект

- Аннотации типов в подписях функций своих проектов: они понадобятся
  в практикуме темы 5.

## Документация

- [typing — поддержка аннотаций типов](https://docs.python.org/3/library/typing.html)
- [collections.abc](https://docs.python.org/3/library/collections.abc.html)
