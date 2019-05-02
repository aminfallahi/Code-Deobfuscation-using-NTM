from __future__ import absolute_import
import os
from celery import Celery as B
from django.conf import settings as C
os.environ.setdefault('DJANGO_SETTINGS_MODULE','report_builder_demo.settings')
A=B('report_builder_demo')
A.config_from_object('django.conf:settings')
A.autodiscover_tasks(lambda:C.INSTALLED_APPS)