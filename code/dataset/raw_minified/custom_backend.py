from brake.backends import cachebe as A
class B(A.CacheBackend):
	def get_ip(B,request):A=request;return A.META.get('HTTP_TRUE_CLIENT_IP',A.META.get('REMOTE_ADDR'))