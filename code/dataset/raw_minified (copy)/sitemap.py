'Urls for the Zinnia sitemap'
from django.conf.urls import url
from zinnia.views.sitemap import Sitemap as A
B=[url('^$',A.as_view(),name='sitemap')]