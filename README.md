### Запуск:

1. #### Установить зависимости.

2. #### Создать файл `.env` по примеру `.env.template`

3. #### Создать таблицы в БД и заполнить фейковыми данными:
```shell
python create_db_tables.py
```
```shell
python generate_fake_data_for_db.py
```

4. #### Запустить сервер:
```shell
python run_server.py
```