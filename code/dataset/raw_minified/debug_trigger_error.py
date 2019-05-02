from __future__ import absolute_import
from django.views.generic import View
from raven.contrib.django.models import client as B
from sentry.web.frontend.error_500 import Error500View as C
class A(View):
	def get(D,request):
		A=request
		try:raise ValueError('An example error')
		except Exception:B.captureException(request=A)
		return C.as_view()(A)