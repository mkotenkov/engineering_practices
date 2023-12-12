## Описание
* Код до форматирования может быть найден в `before_refactoring.md`
* Ответ линтеров до и после рефакторинг находится в `linting.md`

## Установка пакетного менеджера

```bash
pip install poetry # установка poetry
poetry add --group=dev black flake8 pylint isort # добавление dev зависимостей
poetry add numpy pandas # добавление основных зависимостей
```

## Добавление правил в pyproject.toml
```txt
[tool.black]
line-length = 100

[tool.pylint."FORMAT"]
max-line-length = 100
```
```bash
poetry lock # обновление файла poetry.lock
```

## Развертывание окружения
```bash
poetry install # создание виртуального окружения и разрешение зависимостей
poetry shell # активация окружения
```

## Линтинг кода
```bash
flake8 .
pylint hw1/
```

## Форматирование кода
```bash
isort . 
black .
# и некоторый ручной рефакторинг: добавление док-строк и т.д.
```

## Сборка пакета
```bash
poetry build
```
