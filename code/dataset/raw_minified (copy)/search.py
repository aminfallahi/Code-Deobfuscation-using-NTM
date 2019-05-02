'Urls for the Zinnia search'
from django.conf.urls import url
from zinnia.views.search import EntrySearch as A
B=[url('^$',A.as_view(),name='entry_search')]