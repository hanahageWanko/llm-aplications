start :
	docker compose exec llm-django python manage.py runserver 0.0.0.0:8000
dev:
	docker compose exec llm-django python manage.py runserver 0.0.0.0:8000 --settings=config.settings.development
