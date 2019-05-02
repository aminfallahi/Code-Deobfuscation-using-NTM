from django.conf.urls import patterns,url
from tenant_tutorial.views import HomeView as A
B=[url('^$',A.as_view())]