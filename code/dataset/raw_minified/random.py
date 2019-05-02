'Urls for Zinnia random entries'
from django.conf.urls import url
from zinnia.views.random import EntryRandom as A
B=[url('^$',A.as_view(),name='entry_random')]