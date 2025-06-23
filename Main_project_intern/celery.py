import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Main_project_intern.settings')

app = Celery('Main_project_intern')
app.config_from_object('django.conf.settings', namespace='CELERY')
app.autodiscover_tasks()
