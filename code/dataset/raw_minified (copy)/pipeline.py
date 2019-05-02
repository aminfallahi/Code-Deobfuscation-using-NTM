from django.shortcuts import redirect as D
from social.pipeline.partial import partial as A
@A
def B(strategy,details,user=None,is_new=False,*F,**E):
	C='email';A=details
	if E.get('ajax')or user and user.email:return
	elif is_new and not A.get(C):
		B=strategy.request_data().get(C)
		if B:A[C]=B
		else:return D('require_email')