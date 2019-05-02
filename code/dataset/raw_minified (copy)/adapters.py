F=True
E='ACCOUNT_ALLOW_REGISTRATION'
D=getattr
from django.conf import settings as A
from allauth.account.adapter import DefaultAccountAdapter as B
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter as C
class G(B):
	def is_open_for_signup(B,request):return D(A,E,F)
class H(C):
	def is_open_for_signup(B,request,sociallogin):return D(A,E,F)