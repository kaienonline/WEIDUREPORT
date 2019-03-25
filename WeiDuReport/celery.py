# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:yhq

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WeiDuReport.settings')

app = Celery('report')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# app.config_from_object('WeiDuReport.celeryconfig')
app.config_from_object('django.conf:settings')
# Load task modules from all registered Django app configs.
# app.autodiscover_tasks(['report'])
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'report.tasks.get_report',
#         'schedule': 30.0,
#         'args': (16, 16)
#     },
# }
# app.conf.timezone = 'UTC'

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
