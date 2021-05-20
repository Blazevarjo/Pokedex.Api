release: python manage.py migrate
web: gunicorn pokedex.wsgi --log-file -
worker: celery -A pokedex worker --loglevel=INFO