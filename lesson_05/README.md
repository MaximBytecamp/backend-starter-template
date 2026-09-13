# Занятие 5 · окружение, модули и пакеты

Работа по теме 2 «Структура проекта»: всё, что разбиралось в книге занятия,
вы повторяете на своём маленьком проекте.

**Разобрали:** зачем нужно отдельное окружение и как `.venv` меняет поиск
пакетов, выбор интерпретатора в VS Code, `pip` и PyPI на примере Rich, модуль
как файл с одной обязанностью, `import` и `__name__`, пакет и `__init__.py`,
запуск через `python -m`, `requirements.txt`, `.gitignore` и тесты на unittest.

Книга темы:
https://algorthimization-course-vvodnoe.vercel.app/mdk0101-razrabotka-modulei/lessons/02-struktura-python-proekta/index.html

## Что лежит в папке

```
start/trip.py      заготовка: один файл, в нём данные, расчёты и вывод
homework_05.md     домашнее задание
```

Данные внутри файла, внешних зависимостей нет. Проверьте, что заготовка
запускается:

```bash
cd lesson_05/start
python3 trip.py
```

Должен напечататься отчёт: 10 записей, 7900 ₽ всего, 790.00 ₽ средняя трата.
Если чисел нет, вы запустились из другой папки.

---

# Порядок работы

Команды даны для macOS и Linux. На Windows вместо `python3` пишите `py`,
а вместо `source .venv/bin/activate` — `.venv\Scripts\activate`.

## Шаг 0. Забрать новую папку из шаблона

Папка `lesson_05/` появилась в шаблоне после того, как вы завели свой
репозиторий. Заберите её к себе:

```bash
git remote add upstream https://github.com/MaximBytecamp/backend-starter-template.git
git fetch upstream
git checkout upstream/main -- lesson_05
```

`git remote add` нужен один раз, дальше хватит `git fetch upstream`.

## Шаг 1. Ветка на задание

```bash
git switch -c hw-05
```

## Шаг 2. Рабочая папка и окружение

Заготовку копируем, оригинал в `start/` не трогаем: к нему удобно вернуться
и сравнить.

```bash
cp -r lesson_05/start lesson_05/trip-report
cd lesson_05/trip-report
python3 -m venv .venv
source .venv/bin/activate
```

Проверка: в начале строки появилось `(.venv)`, а команда
`python -c "import sys; print(sys.executable)"` печатает путь внутри `.venv`.
Этот вывод понадобится для README, скопируйте его сразу.

## Шаг 3. Поставить зависимость

```bash
pip install rich
pip freeze > requirements.txt
```

Rich нужен для вывода отчёта таблицей. Загляните в `requirements.txt`: там
окажется не одна строка, потому что у Rich есть свои зависимости.

## Шаг 4. Разрезать файл на модули и собрать пакет

Раскладка та же, что в книге:

```
app/__init__.py
app/main.py                   точка входа: собирает расчёты и печатает отчёт
app/services/__init__.py
app/services/calculator.py    только расчёты, ничего не печатает
app/utils/__init__.py
app/utils/formatter.py        только оформление текста
tests/test_calculator.py
```

Данные пока оставьте списком в `app/main.py`. Правило деления одно: у модуля
одна обязанность, и расчёты не печатают, а возвращают значения.

Проверка: `python -m app.main` печатает тот же отчёт, что и заготовка.
А вот `python app/main.py` упадёт с `ModuleNotFoundError`, и это правильное
поведение: при прямом запуске файла корень проекта не попадает в пути поиска,
поэтому пакет `app` не находится. Разбор этого места — в главе 2.5.

## Шаг 5. Дописать два расчёта

Это и есть содержательная часть задания, она описана в `homework_05.md`.

## Шаг 6. Тесты

```bash
python -m unittest discover -s tests -v
```

Не меньше пяти тестов, и все проходят.

## Шаг 7. Проверить воспроизводимость

Скопируйте проект в чистую папку **без** `.venv`, создайте окружение заново,
поставьте зависимости из `requirements.txt` и запустите. Команды и результат
запишите в свой `README.md`.

## Шаг 8. Сдать

```bash
cd ../..
git add lesson_05
git commit -m "hw-05: окружение, пакет и тесты для отчёта по поездке"
git push -u origin hw-05
```

Дальше на GitHub открываете Pull Request в свою `main`. В описании коротко:
какие модули получились и почему вы провели границы именно так.

То же самое мышкой в VS Code: [коротко](../docs/git/README.md) ·
[подробно](../docs/git/FULL.md).
