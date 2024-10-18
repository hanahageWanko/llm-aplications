start :
	docker compose exec llm-django python manage.py runserver 0.0.0.0:8000
dev:
	docker compose exec llm-django python manage.py runserver 0.0.0.0:8000 --settings=config.settings.development
mv-model-and-view:
	mkdir src/app/models
	touch src/app/models/__init__.py
	rm src/app/models.py
	mkdir src/app/views
	touch src/app/views/__init__.py
	rm src/app/views.py