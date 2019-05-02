'Urls for the Zinnia trackback'
from django.conf.urls import url
from zinnia.views.trackback import EntryTrackback as A
B=[url('^(?P<pk>\\d+)/$',A.as_view(),name='entry_trackback')]