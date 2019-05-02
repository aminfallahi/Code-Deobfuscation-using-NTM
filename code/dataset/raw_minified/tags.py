'Urls for the Zinnia tags'
from django.conf.urls import url as A
from zinnia.urls import _
from zinnia.views.tags import TagList as C
from zinnia.views.tags import TagDetail as B
D=[A('^$',C.as_view(),name='tag_list'),A('^(?P<tag>[^/]+(?u))/$',B.as_view(),name='tag_detail'),A(_('^(?P<tag>[^/]+(?u))/page/(?P<page>\\d+)/$'),B.as_view(),name='tag_detail_paginated')]