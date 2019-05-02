from .django_urls import *
from django.conf.urls import include,url
urlpatterns+=[url('^',include('wooey.urls'))]