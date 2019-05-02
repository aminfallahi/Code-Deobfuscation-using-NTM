F='restricted'
E='pypi'
D='simple'
from django.conf import settings as B
from django_hosts import patterns as C,host as A
G=C('',A('www',B.ROOT_URLCONF,name='default'),A(D,'packages.simple.urls',name=D),A(E,'pypi.simple.urls',name=E),A(F,'packages.simple.restricted_urls',name=F))