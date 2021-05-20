import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokedex.settings')
app = Celery('pokedex')

app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

