from datetime import datetime as C
class A:
	def process_view(D,request,callback,callback_args,callback_kwargs):
		A=request
		if not A.user.is_anonymous()and A.path=='/':B=A.user.userprofile;B.last_active=C.now();B.save()