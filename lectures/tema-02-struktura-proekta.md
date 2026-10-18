# Тема 2 · Структура проекта: окружение, модули и пакеты

**Книга темы:** https://algorthimization-course-vvodnoe.vercel.app/mdk0101-razrabotka-modulei/lessons/02-struktura-python-proekta/index.html

**Файлы занятия:** [materials/tema-02-struktura-proekta](../materials/tema-02-struktura-proekta/) —
стартовый файл, разрозненные файлы для практики и итоговая раскладка
на Python и на Go.

**Задание в репозитории:** [`lesson_02`](../lesson_02/README.md) — своё окружение и первый модуль.

## Содержание книги

Книга из восьми глав. Переключатель **Python / Go** в левой колонке меняет
язык всего материала; задачи и ожидаемые результаты в обеих ветках одинаковые.

### 2.1 Виртуальное окружение

Пакеты, установленные в общий Python, мешают друг другу: разным проектам
нужны разные версии. **Виртуальное окружение** `.venv` — папка проекта
со своим интерпретатором и своими пакетами.

| Шаг | macOS / Linux | Windows (PowerShell) |
|---|---|---|
| создать | `python3 -m venv .venv` | `py -m venv .venv` |
| активировать | `source .venv/bin/activate` | `.venv\Scripts\activate` |
| проверить | `python -c "import sys; print(sys.executable)"` | то же |

После активации в начале строки терминала появляется `(.venv)`, а путь
к интерпретатору указывает внутрь `.venv`.

### 2.2 VS Code

Редактор и терминал выбирают интерпретатор независимо. В VS Code его
выбирают командой **Python: Select Interpreter** и указывают `.venv`;
окружение можно создать и из палитры команд.

### 2.3 Зависимости

`python -m pip install rich` ставит библиотеку Rich из PyPI в активное
окружение. Запуск через `python -m pip` гарантирует, что пакет попадёт
в тот же Python, которым запускается программа. Поле `Location` в выводе
`pip show rich` показывает, куда пакет установлен.

### 2.4 Модули

**Модуль** — файл `.py` с одной обязанностью. Функции переносят из одного
большого файла в модули, сохраняя поведение. `import` выполняет модуль один
раз; повторный импорт файл не выполняет. Строка
`if __name__ == "__main__":` отделяет код, который выполняется только при
прямом запуске файла.

### 2.5 Пакеты

**Пакет** — папка с модулями и файлом `__init__.py`. Импорты пишутся
абсолютными: `from app.services.calculator import calculate_average`.
Проект запускается командой `python -m app.main` из корня; прямой запуск
`python app/main.py` падает с `ModuleNotFoundError`, потому что корень
проекта не попадает в пути поиска.

```text
app/__init__.py
app/main.py                   точка входа
app/services/calculator.py    только расчёты, ничего не печатает
app/utils/formatter.py        только оформление вывода
tests/test_calculator.py
requirements.txt
README.md
```

### 2.6 Воспроизводимость

`pip freeze > requirements.txt` записывает список зависимостей с версиями,
`pip install -r requirements.txt` восстанавливает их. `.venv` в Git
не попадает: его исключает `.gitignore`. README описывает, как поднять проект
с нуля. Тесты проверяют расчёты: функции с `assert`, запуск
`python -m pytest -v`. Итоговая проверка — скачать проект в пустую папку,
создать новое окружение и запустить.

## Что делали на занятии

1. Создали и активировали `.venv`, выбрали интерпретатор в VS Code.
2. Установили Rich и проверили, что он лежит внутри окружения.
3. Разложили один файл Student Tools на модули и собрали пакет `app`.
4. Записали `requirements.txt`, `.gitignore`, README, добавили тесты.
5. Практика: восстановили проект из разрозненных файлов с неудачными
   именами, не меняя функций.

## Что вошло в проект

- Задание 2 ([`lesson_02`](../lesson_02/README.md)): папка `trip` —
  окружение `.venv`, Rich в `requirements.txt`, расчёты вынесены в модуль
  `calculator.py`, README с командами запуска.

## Документация

- [venv](https://docs.python.org/3/library/venv.html)
- [Python Tutorial: модули и пакеты](https://docs.python.org/3/tutorial/modules.html)
- [Rich](https://rich.readthedocs.io/)
- [Python в VS Code](https://code.visualstudio.com/docs/python/environments)
