from settings import *
INSTALLED_APPS.append('gis')
DATABASES={'default':{'ENGINE':'django.contrib.gis.db.backends.postgis','NAME':DATABASE_NAME}}
ROOT_URLCONF='gis.urls'