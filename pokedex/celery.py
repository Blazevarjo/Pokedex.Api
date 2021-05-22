import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokedex.settings')

app = Celery('pokedex')

app.conf.update(BROKER_URL=settings.BROKER_URL,
                CELERY_RESULT_BACKEND=settings.BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
