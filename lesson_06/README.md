# Занятие 6 · Проверка типов: Pylance и mypy

Практическая работа по главе 4.3. Вы включаете проверку типов в VS Code,
находите ошибки в редакторе и в терминале, снимаете экран на каждом шаге
и заполняете готовый отчёт.

Глава 4.3:
https://algorthimization-course-vvodnoe.vercel.app/mdk0101-razrabotka-modulei/lessons/04-docstrings-i-dokumentaciya/03-proverka-tipov.html

## Что лежит в папке

```
otchet_06.md     отчёт: текст написан, вы вписываете свои данные и кладёте снимки
img/             заглушки снимков, их заменяете своими снимками
rezhimy.py       файл для шага 5: шесть ошибок разного рода
```

Папка `lesson_06` появилась в шаблоне после того, как вы завели свой
репозиторий. Забрать её проще всего кнопками: на GitHub в шаблоне
**Code → Download ZIP**, распаковать и положить папку `lesson_06` к себе
в проект. Если в вашем репозитории нет папки
`materials/tema-04-annotacii-tipov`, возьмите её из того же архива.

## Подготовка проекта

1. Скопируйте папку `materials/tema-04-annotacii-tipov/otchet-kafe-start`
   в `lesson_06/`. Это второй архив проекта «Отчёт кафе», аннотации в нём
   расставлены.
2. Откройте в VS Code именно папку `lesson_06/otchet-kafe-start`
   (**File → Open Folder**). Настройки редактора и mypy читаются из корня
   открытой папки.
3. Создайте окружение и установите зависимости, как в главе 4.1:

   | macOS / Linux | Windows |
   |---|---|
   | `python3 -m venv .venv` | `py -m venv .venv` |
   | `.venv/bin/pip install -r requirements.txt` | `.venv\Scripts\pip install -r requirements.txt` |

## Ход работы

Каждый шаг соответствует параграфу главы 4.3. После шага сделайте снимок
и положите его в `lesson_06/img/` под именем из таблицы: файл с тем же именем
уже лежит там как заглушка, его нужно заменить.

| Шаг | Что сделать | Глава | Снимок |
|---|---|---|---|
| 1 | Создать в корне проекта `proba.py` с двумя неверными вызовами. Выбрать интерпретатор `.venv` (**Python: Select Interpreter**). Убедиться, что в режиме `off` подчёркиваний нет | §2, §3 шаги 1–3 | `06-01-off.png`: файл `proba.py` без подчёркиваний, внизу справа надпись `.venv` |
| 2 | Включить режим `basic` на вкладке **Workspace** и открыть `.vscode/settings.json` | §3 шаг 4 | `06-02-settings.png`: файл `settings.json`, последняя строка `"python.analysis.typeCheckingMode": "basic"` |
| 3 | Вернуться в `proba.py`, посмотреть на подчёркивания и навести указатель на `40` | §3 шаги 5–6 | `06-03-squiggle.png`: два подчёркнутых аргумента и цифра 2 на вкладке; `06-04-hover.png`: сообщение Pylance над `40` |
| 4 | Добавить в `proba.py` вызов своего варианта (таблица ниже) и открыть панель **Problems** | §3 шаг 7 | `06-05-problems.png`: панель Problems, у `proba.py` три ошибки |
| 5 | Скопировать `rezhimy.py` в корень проекта, открыть его и по очереди выбрать режимы `off`, `basic`, `standard`, `strict`. Записать число сообщений в панели Problems. После опыта вернуть `basic` | §4 | `06-06-strict.png`: `rezhimy.py` в режиме `strict` с открытой панелью Problems |
| 6 | В терминале проверить `proba.py` командой mypy | §5 шаги 1–2 | `06-07-mypy-errors.png`: версия mypy, три строки `error` и итог `Found 3 errors` |
| 7 | Исправить все три вызова, сохранить файл, снова проверить `proba.py`, затем пакет `app` | §5 шаги 4–5 | `06-08-mypy-success.png`: две строки `Success` |
| 8 | Проверить mypy первый архив, где аннотаций нет | §8 | `06-09-bez-tipov.png`: список ошибок `no-untyped-def` и итог `Found 17 errors` |
| 9 | Заменить содержимое `proba.py` кодом из §9 главы (вызов `grade_bounds` и строка `reveal_type(bounds)`), сохранить и выполнить `mypy proba.py`. Затем, не закрывая терминал, навести указатель на `bounds` в редакторе | §9 | `06-10-tip.png`: подсказка над `bounds` и строка `Revealed type` в терминале на одном снимке |

Команды терминала для шагов 6–8:

| Шаг | macOS / Linux | Windows |
|---|---|---|
| 6 | `.venv/bin/mypy --version && .venv/bin/mypy proba.py` | `.venv\Scripts\mypy --version; .venv\Scripts\mypy proba.py` |
| 7 | `.venv/bin/mypy proba.py && .venv/bin/mypy app` | `.venv\Scripts\mypy proba.py; .venv\Scripts\mypy app` |
| 8 | `.venv/bin/mypy ../../materials/tema-04-annotacii-tipov/otchet-kafe-bez-tipov/app` | `.venv\Scripts\mypy ..\..\materials\tema-04-annotacii-tipov\otchet-kafe-bez-tipov\app` |

На шаге 8 mypy запускается из папки второго архива и берёт из его
`pyproject.toml` параметр `disallow_untyped_defs = true`. Поэтому функции
первого архива без аннотаций считаются ошибками.

## Вариант для шага 4

Вариант — остаток от деления вашего номера в журнале на 6; если остаток 0,
вариант 6. Строку импорта поставьте второй строкой файла, вызов — последней.

| Вариант | Импорт | Вызов с ошибкой |
|---|---|---|
| 1 | `from app.utils.text import normalize_name` | `name = normalize_name(42)` |
| 2 | `from app.services.calculator import calculate_average` | `avg = calculate_average("5, 4, 3")` |
| 3 | `from app.services.orders import revenue_by_waiter` | `top = revenue_by_waiter([], top="3")` |
| 4 | `from app.services.report_file import save_report` | `size = save_report("report.txt", ["Итог"])` |
| 5 | `from app.ui.console import print_report` | `print_report("Итог")` |
| 6 | `from app.utils.formatter import format_title` | `title2 = format_title("Итог", "40")` |

Подпись функции из своего варианта найдите в модуле, откуда она
импортирована: по ней видно, какой тип нужно передать при исправлении
на шаге 7.

## Как делать снимки

- Снимок окна VS Code целиком, а не всего экрана: на macOS
  **Cmd + Shift + 4**, затем пробел и щелчок по окну; на Windows
  **Win + Shift + S**, режим «Окно».
- Текст на снимке должен читаться без увеличения. Если окно большое,
  уменьшите его до половины экрана перед снимком.
- Формат PNG, имя — строго из таблицы. Тогда снимок встанет в отчёт сам.

## Отчёт

Откройте [`otchet_06.md`](otchet_06.md). Текст отчёта написан, на месте `___`
впишите свои данные: номер варианта, числа из панели Problems, строки
из терминала, исправленный вызов. Остальной текст не меняйте.
Просмотреть результат можно в VS Code: **Cmd/Ctrl + Shift + V**.

## Что сдать

В `lesson_06/`:

- `otchet_06.md` с заполненными `___`;
- `img/` с десятью своими снимками;
- папку `otchet-kafe-start` с файлом `.vscode/settings.json`, где выбран режим `basic`.

Файлы `proba.py`, `rezhimy.py` из корня проекта и папку `.venv`
не добавляйте: `.venv` уже указана в `.gitignore` проекта, а два файла
для опытов удалите после работы.

Сдача: коммит `hw-06: проверка типов` в `main` и отправка на GitHub,
до начала следующего занятия.

## Критерии

| За что | Баллы |
|---|---|
| Режим `basic` включён в настройках проекта, ошибки видны в редакторе (снимки 1–5) | 3 |
| Сравнение четырёх режимов: числа и снимок `strict` | 1 |
| Ошибки найдены и исправлены в терминале, `mypy app` без ошибок (снимки 7–8) | 3 |
| Первый архив проверен, тип выведен двумя способами (снимки 9–10) | 2 |
| Все `___` заполнены, снимки свои и соответствуют варианту | 1 |

Работа со снимками-заглушками возвращается на доработку.
