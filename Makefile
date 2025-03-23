start :
	docker compose exec llm-django python manage.py runserver 0.0.0.0:8000

backend-dev:
	docker compose exec llm-django python manage.py runserver 0.0.0.0:8000 --settings=config.settings.development

mv-model-and-view:
	mkdir src/app/models
	touch src/app/models/__init__.py
	rm src/app/models.py
	mkdir src/app/views
	touch src/app/views/__init__.py
	rm src/app/views.py

migrate:
	docker compose exec llm-django python manage.py migrate --settings=config.settings.development

make:
	docker compose exec llm-django python manage.py makemigrations --settings=config.settings.development

dbshell:
	docker compose exec llm-django python manage.py dbshell --settings=config.settings.development

installed-packages:
	docker compose exec llm-django pip freeze

init-tailwind:
	docker compose exec llm-django python manage.py tailwind init --settings=config.settings.development

install-tailwind:
	docker compose exec llm-django python manage.py tailwind install --settings=config.settings.development

front-start:
	docker compose exec llm-django python manage.py tailwind start --settings=config.settings.development

dev:
	@make backend-dev
	@make front-start

collectstatic:
	docker compose exec llm-django python manage.py collectstatic --settings=config.settings.development

build:
	@make collectstatic
