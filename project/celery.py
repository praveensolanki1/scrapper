from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')


app = Celery('project')
app.config_from_object('django.conf:settings',namespace='celery')
app.conf.beat_schedule={
    
        'task':'get_data',
        'schedule':crontab(hour=23,minute=59),
}
app.autodiscover_tasks()

