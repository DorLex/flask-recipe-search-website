server:
	python main.py

up-db:
	docker compose up -d

init-db-data:
	python -m faker.service
