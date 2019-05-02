from django.core.handlers.base import BaseHandler as A
class B(A):
	'Required to process request and response middleware'
	def __call__(A,request):
		C=request;A.load_middleware();B=A.get_response(C)
		for D in A._response_middleware:B=D(C,B)
		return B