release: python manage.py migrate
web: gunicorn pokedex.wsgi --log-file -
beat: celery -A pokedex beat --loglevel=INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
