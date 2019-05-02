'\nWSGI config for {{ cookiecutter.repo_name }} project.\n\nIt exposes the WSGI callable as a module-level variable named ``application``.\n\nFor more information on this file, see\nhttps://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/\n'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','{{ cookiecutter.repo_name }}.settings.production')
from django.core.wsgi import get_wsgi_application as A
B=A()