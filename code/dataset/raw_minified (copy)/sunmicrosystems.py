from ztag.annotation import *
class SunMicroSystems(Annotation):
	protocol=protocols.HTTPS;subprotocol=protocols.HTTPS.TLS;port=None
	def process(self,obj,meta):
		C='issuer';B='parsed';A='certificate';organization=obj[A][B][C]['organization'][0];common_name=obj[A][B][C]['common_name'][0]
		if'Sun Microsystems'in organization:meta.global_metadata.manufacturer=Manufacturer.SUN_MICROSYSTEMS;return meta