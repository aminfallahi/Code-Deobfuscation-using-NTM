from django.conf.urls import patterns as A,url
B=A('',url('^simple/$','django.shortcuts.render',name='simple-direct'))