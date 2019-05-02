B='sample_view'
from django.conf.urls import patterns as C,url as A
D=C('urldecorators.tests.views',A('^$',B),A('^args/(\\d+)/(\\d+)/$',B),A('^kwargs/(?P<inc_inc_arg1>\\d+)/(?P<inc_inc_arg2>\\d+)/$',B))