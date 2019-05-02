from threading import local
A=local()
def B():return getattr(A,'request',None)
class C:
	'\n    Middleware that stores the request object in thread local storage.\n    '
	def process_request(B,request):A.request=request