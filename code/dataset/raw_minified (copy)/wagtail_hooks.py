from __future__ import absolute_import,unicode_literals
from django.conf.urls import include as A,url
from wagtail.wagtailcore import hooks
from .  import urls
@hooks.register('register_admin_urls')
def B():B='wagtailsettings';return[url('^settings/',A(urls,app_name=B,namespace=B))]