B=None
from braces.views import LoginRequiredMixin as A
from django.contrib import messages as C
class D(A):
	login_message=B
	def no_permissions_fail(A,request=B):
		if A.login_message is not B:C.info(A.request,A.login_message)
		return super().no_permissions_fail(request=request)