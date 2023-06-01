# conversion/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conversion.settings")
app = Celery("conversion")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()