from django.conf.urls import patterns, url
from customers.views import TenantView

urlpatterns = [
        url(r'^$', TenantView.as_view()),
    ]
