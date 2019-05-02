from django.conf.urls import patterns as C,include as B,url
from tastypie.api import Api
from packages.api import PackageResource as D,ReleaseResource as E
A=Api(api_name='v1')
A.register(D())
A.register(E())
F=C('',url('',B(B(A.urls))))