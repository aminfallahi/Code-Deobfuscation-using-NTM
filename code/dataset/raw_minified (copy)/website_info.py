from django import template as A
from django.conf import settings as B
C=A.Library()
@C.simple_tag
def D(name):return B.WEBSITE_INFO[name]