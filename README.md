## Описание:

Сайт с интерактивным поиском кулинарных рецептов по имеющимся у вас ингредиентам.

Написан на Flask.

## Запуск:

1. Установить зависимости из `requirements.txt`.

2. Запустить предпочитаемую БД.

3. Создать файл `.env` по примеру `.env.template`.

4. Создать таблицы в БД и заполнить фейковыми данными:
   ```shell
   python create_db_tables.py
   ```

   ```shell
   python generate_fake_data_for_db.py
   ```

5. Запустить сервер:
   ```shell
   python run_server.py
   ```
