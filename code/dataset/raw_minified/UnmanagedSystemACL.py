from django.core.exceptions import PermissionDenied
from MozInvAuthorization.BaseACL import BaseACL as A
from settings import USER_SYSTEM_ALLOWED_DELETE as C
class B(A):
	def __init__(A,request):
		B=request;A.request=B
		if B.user.username and B.user.username!='':A.user=A.request.user.username
		else:A.user=A.request.META['REMOTE_USER']
	def check_delete(B,allowed=None):
		A=allowed
		if A:A=A
		else:A=C
		B.check_for_permission(B.user,A)