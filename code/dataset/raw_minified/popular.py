from django.conf.urls import patterns as C,url as A
from cab.views import popular as B
D=C('',A('^languages/$',B.top_languages,name='cab_top_languages'),A('^bookmarked/$',B.top_bookmarked,name='cab_top_bookmarked'),A('^rated/$',B.top_rated,name='cab_top_rated'))