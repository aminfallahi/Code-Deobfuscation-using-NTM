from __future__ import absolute_import
import os
from celery import Celery as B
os.environ.setdefault('DJANGO_SETTINGS_MODULE','settings')
from django.conf import settings as C
A=B('sandbox')
A.config_from_object('django.conf:settings')
A.autodiscover_tasks(lambda:C.INSTALLED_APPS)