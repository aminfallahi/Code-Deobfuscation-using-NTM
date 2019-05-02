from django.conf.urls import patterns as A,url
from piston.resource import Resource as B
from opps.api import ApiKeyAuthentication as C
from .api import LoggingHandler as D
E=B(handler=D,authentication=C())
F=A('',url('^api/contrib/logging/$',E,{'emitter_format':'json'}))