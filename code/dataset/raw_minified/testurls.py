from django.conf.urls import patterns as A,url,include as B
C=A('',url('^addressbook/',B('addressbook.urls')))