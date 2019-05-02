from django.conf.urls import patterns as A,url,include
from django.contrib.auth.decorators import login_required as B
from .views import process_rating as C
from .views import next_practice_item as D
E=A('',url('^(?P<deck_id>\\d+)/$',B(D.as_view(template_name='learning/learn_item.html')),name='learning'),url('^rate$',C,name='learning_post'))