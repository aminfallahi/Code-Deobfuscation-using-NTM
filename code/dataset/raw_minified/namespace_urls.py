from django.conf.urls import patterns as A,url
from tests import views
B=A('',url('^$',views.PostViewSet.as_view({'get':'list'}),name='post-list'))