try:from django.conf.urls import patterns,url
except ImportError:from django.conf.urls.defaults import patterns,url
from subdomains.tests.urls.default import urlpatterns as A
B=A