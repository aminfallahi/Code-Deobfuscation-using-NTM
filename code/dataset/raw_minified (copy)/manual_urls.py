from django.conf.urls import include as A,url
from core.tests.resources import NoteResource as B
C=B()
D=[url('^',A(C.urls))]