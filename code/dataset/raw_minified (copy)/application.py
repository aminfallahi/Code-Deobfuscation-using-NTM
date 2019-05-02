import os,django.core.handlers.wsgi
os.environ['DJANGO_SETTINGS_MODULE']='config.deployed.settings'
A=django.core.handlers.wsgi.WSGIHandler()