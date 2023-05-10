up:
	docker-compose up -d

down:
	docker-compose down

migrate:
	docker-compose run web python manage.py migrate

makemigrations:
	docker-compose run web python manage.py makemigrations

shell:
	docker-compose run web python manage.py shell

test:
	docker-compose run web python manage.py test