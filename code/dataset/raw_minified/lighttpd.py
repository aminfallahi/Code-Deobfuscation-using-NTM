from ztag.annotation import *
class Lighttpd(Annotation):
	protocol=protocols.HTTP;subprotocol=protocols.HTTP.GET;port=None
	def process(self,obj,meta):
		B='/';A='lighttpd';server=obj['headers']['server']
		if A in server:
			meta.local_metadata.product=A
			if B in server:meta.local_metadata.version=server.split(B)[1].strip()
			return meta