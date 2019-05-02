from uliweb import Middleware as A
from uliweb.orm import set_dispatch_send as B,set_echo as C
class D(A):
	ORDER=70
	def process_request(A,request):C(False);B(True)