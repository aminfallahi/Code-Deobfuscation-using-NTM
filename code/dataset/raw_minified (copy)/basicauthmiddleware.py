from django.contrib.auth import authenticate as E,login as F,logout as A
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
class B:
	def process_request(J,request):
		C=request;D=C.META.get('HTTP_AUTHORIZATION')
		if D:
			G,A=D.split(' ',1)
			if'basic'==G.lower():
				A=A.strip().decode('base64');H,I=A.split(':',1);B=E(username=H,password=I)
				if B is not None:
					if B.is_active:F(C,B)