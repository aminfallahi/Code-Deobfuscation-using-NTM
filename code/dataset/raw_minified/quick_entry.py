'Url for the Zinnia quick entry view'
from django.conf.urls import url
from zinnia.urls import _
from zinnia.views.quick_entry import QuickEntry as A
B=[url(_('^quick-entry/$'),A.as_view(),name='entry_quick_post')]