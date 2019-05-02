from django.conf.urls import patterns,url
from customers.views import TenantView as A
B=[url('^$',A.as_view())]