F='cardbox/deck/deck_form.html'
from django.conf.urls import patterns as D,url as A,include
from django.contrib.auth.decorators import login_required as B
from .views import PracticeDeckList as E
from cardbox import deck_views as C
G=D('',A('^$',B(E.as_view(template_name='cardbox/deck/deck_list.html')),name='deck_list'),A('^new$',B(C.DeckCreate.as_view(template_name=F)),name='deck_new'),A('^edit/(?P<pk>\\d+)$',B(C.DeckUpdate.as_view(template_name=F)),name='deck_edit'),A('^delete/(?P<pk>\\d+)$',B(C.DeckDelete.as_view(template_name='cardbox/deck/deck_confirm_delete.html')),name='deck_delete'),A('^detail/(?P<pk>\\d+)/$',B(C.DeckDetailView.as_view(template_name='cardbox/deck/deck_detail.html')),name='deck_detail'))