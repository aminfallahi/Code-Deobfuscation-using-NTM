from uliweb import Middleware as A
class B(A):
	ORDER=100
	def process_request(B,request):from uliweb.contrib.auth import get_user as A;request.user=A()