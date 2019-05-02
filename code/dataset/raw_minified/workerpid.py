import os
from wsgid.interfaces.filters import IPostRequestFilter as A
from wsgid.core import Plugin as B
class C(B):
	'\n     Simple fillter that adds one more response header containing the\n     pid of the Wsgid workers that was running the WSGI application\n    ';implements=[A]
	def process(A,message,status,headers,body):return status,headers+[('X-Worker',os.getpid())],body
	def exception(A,message,e):0