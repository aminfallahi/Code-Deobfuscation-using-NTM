import warnings as A
__all__='DBLogMiddleware',
class B:
	'We now use signals'
	def process_exception(B,request,exception):A.warn('DBLogMiddleware is no longer used.',DeprecationWarning)