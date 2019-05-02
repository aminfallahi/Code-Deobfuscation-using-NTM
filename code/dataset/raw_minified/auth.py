'\nAuthentication view decorators.\n\n'
from django.conf import settings as B
from django.contrib.auth.decorators import login_required as C
def A(viewfunc):
	'no-op if settings.ALLOW_ANONYMOUS_ACCESS, else login_required';A=viewfunc
	if B.ALLOW_ANONYMOUS_ACCESS:return A
	return C(A)