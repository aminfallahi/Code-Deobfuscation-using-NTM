from django.conf.urls import patterns as A,url
from .views import Verify as B
C=A('',url('^browserid/verify/',B.as_view(),name='browserid_verify'))