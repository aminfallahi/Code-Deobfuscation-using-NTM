from django.conf.urls import url
from django.http import HttpResponse as A
def B(reqeust):return A(content='Hello Word',content_type='text/plain')
C=[url('^hello$',B)]