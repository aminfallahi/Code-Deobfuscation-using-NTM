from django.conf.urls import url
from django.views import defaults as A
from openstack_dashboard.urls import urlpatterns as B
B.append(url('^500/$',A.server_error))