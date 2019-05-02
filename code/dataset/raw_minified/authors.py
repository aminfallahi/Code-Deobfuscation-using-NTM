'Urls for the Zinnia authors'
from django.conf.urls import url as A
from zinnia.urls import _
from zinnia.views.authors import AuthorList as C
from zinnia.views.authors import AuthorDetail as B
D=[A('^$',C.as_view(),name='author_list'),A(_('^(?P<username>[.+-@\\w]+)/page/(?P<page>\\d+)/$'),B.as_view(),name='author_detail_paginated'),A('^(?P<username>[.+-@\\w]+)/$',B.as_view(),name='author_detail')]