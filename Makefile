all: build migrate static

build:
	docker build -t metrics-api:v0 .

migrate:
	docker run --env-file env metrics-api:v0 sh -c "python manage.py makemigrations && python manage.py migrate"
	python manage.py createsuperuser

static:
	docker run --env-file env metrics-api:v0 sh -c "python manage.py collectstatic --noinput"

run:
	docker run --env-file env -p 80:8000 metrics-api:v0

dev:
	python3 manage.py runserver 127.0.0.1:8080
