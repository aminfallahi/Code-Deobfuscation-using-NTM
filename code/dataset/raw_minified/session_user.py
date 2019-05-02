from django.contrib.auth.models import User
from django.contrib.sessions.models import Session as E
def A(request):
	D=None;A=E.objects.filter(session_key=request.COOKIES.get('sessionid'))
	if not A:return D
	B=A[0].get_decoded().get('_auth_user_id')
	if not B:return D
	C=User.objects.filter(pk=B)
	if not C:return D
	return C[0]