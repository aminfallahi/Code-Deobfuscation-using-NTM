from ztag.annotation import *
class MRV1Server(Annotation):
	protocol=protocols.HTTP;subprotocol=protocols.HTTP.GET;port=None
	def process(self,obj,meta):
		A='Mrvl';s=obj['headers']['server']
		if s.startswith(A):meta.local_metadata.product=A;v=s.split('-')[1].replace('_','.');meta.local_metadata.version=v;return meta