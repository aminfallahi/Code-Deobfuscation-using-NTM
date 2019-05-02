import warnings as A
A.warn('The localeurl_future templatetag library is deprecated; use localeurl_tags instead.',DeprecationWarning)
from django import template as B
from localeurl_tags import locale_url as C
D=B.Library()
D.tag('locale_url',C)