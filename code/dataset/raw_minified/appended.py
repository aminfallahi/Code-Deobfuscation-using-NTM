C='special'
from django_hosts import patterns as A,host
from tests.hosts.simple import host_patterns as B
B+=A('',host(C,'tests.urls.simple',name=C))