import mimetypes as B
from pump.util import response as C
def A(app,options={}):
	def A(req):
		A=app(req)
		if not A or A.get('headers',{}).get('content_type'):return A
		D,E=B.guess_type(req['uri']);return C.with_content_type(A,D or'application/octet-stream')
	return A