# Makefile

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

migrate:
	docker-compose exec web python manage.py migrate

makemigrations:
	docker-compose exec web python manage.py makemigrations

createsuperuser:
	docker-compose exec web python manage.py createsuperuser

shell:
	docker-compose exec web python manage.py shell

collectstatic:
	docker-compose exec web python manage.py collectstatic --noinput

embed:
	docker-compose exec web python src/embedding.py

reset-db:
	docker-compose down -v
	docker-compose up -d
	docker-compose exec web python manage.py migrate

restart:
	docker-compose restart

build:
	docker-compose build
