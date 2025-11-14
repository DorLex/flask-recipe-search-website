## Сайт с поиском кулинарных рецептов.

### Описание:

Сайт с интерактивным поиском кулинарных рецептов по имеющимся у вас ингредиентам.

### Стек:

- `Flask`
- `Flask-SQLAlchemy`
- `pydantic-settings`
- `HTML`, `CSS`, `JavaScript`

### Установка зависимостей:

1. Создать окружение через `poetry`:
    ```shell
    poetry env use python3.12
    ```

2. Активировать окружение: *(можно и через `poetry shell`, но `shell` в последних версиях является плагином, и не
   предустановлен)*
    ```shell
    eval $(poetry env activate)
    ```

3. Установить только основные зависимости, необходимые для запуска:
   ```shell
   poetry install --no-root --without dev
   ```

4. Установить все зависимости, включая `dev`/`test` (+linter, +pre-commit и т.д.):
    ```shell
    poetry install --no-root
    ```

### Pre-commit, Linter, Formatter:

- Установить `pre-commit` хуки:
    ```shell
    pre-commit install
    ```

- Ручной запуск линтера и форматера:
    ```shell
    ruff check --fix --show-fixes && ruff format
    ```

### Запуск:

1. Создать файл `.env` по примеру `example.env`.

2. Запустить БД:
   ```shell
   make up-db
   ```

3. Проинициализировать БД:
   ```shell
   make init-db-data
   ```

4. Запустить сервер:
   ```shell
   make server
   ```
