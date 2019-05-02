from __future__ import absolute_import,print_function
from django.core.urlresolvers import reverse as B
from sentry.auth.helper import AuthHelper as C
from sentry.web.frontend.base import BaseView as A
class D(A):
	auth_required=False
	def handle(D,request):
		A=C.get_for_request(request)
		if A is None:return D.redirect(B('sentry-login'))
		if not A.pipeline_is_valid():return A.error('Something unexpected happened during authentication.')
		return A.current_step()