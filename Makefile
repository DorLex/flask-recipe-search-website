server:
	python main.py

up-db:
	docker compose up -d

init-db-data:
	python create_db_tables.py && python generate_fake_data_for_db.py
