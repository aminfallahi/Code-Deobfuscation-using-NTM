from django.conf.urls import patterns as A,url
from cab.views import popular as B,snippets as C
D=A('',url('^$',B.top_authors,name='cab_top_authors'),url('^(?P<username>[\\w.@+-]+)/$',C.author_snippets,name='cab_author_snippets'))