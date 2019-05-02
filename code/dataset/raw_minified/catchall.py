from __future__ import absolute_import
from django.http import HttpResponse as A
from django.views.decorators.csrf import csrf_exempt as B
from sentry.api.base import Endpoint as C
class D(C):
	permission_classes=()
	@B
	def dispatch(self,request,*B,**C):return A(status=404)