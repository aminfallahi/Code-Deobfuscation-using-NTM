D=True
from django.conf.urls import patterns as A,url
from packages.simple.views import PackageIndex as B,PackageDetail as C
E='packages.simple.views.not_found'
F=A('',url('^$',B.as_view(restricted=D),name='simple_package_index'),url('^(?P<slug>[^/]+)/(?:(?P<version>[^/]+)/)?$',C.as_view(restricted=D),name='simple_package_detail'))