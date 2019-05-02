from django.conf.urls import patterns as C,url as A
from cab.views import bookmarks as B
D=C('',A('^$',B.user_bookmarks,name='cab_user_bookmarks'),A('^add/(?P<snippet_id>\\d+)/$',B.add_bookmark,name='cab_bookmark_add'),A('^delete/(?P<snippet_id>\\d+)/$',B.delete_bookmark,name='cab_bookmark_delete'))