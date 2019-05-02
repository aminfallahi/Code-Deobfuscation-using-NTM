from ztag.annotation import *
class INTEGJNIOR310(Annotation):
	protocol=protocols.MODBUS;subprotocol=protocols.MODBUS.DEVICE_ID;port=None
	def process(self,obj,meta):
		B='objects';A='mei_response';vendor=obj[A][B]['vendor'].lower();product_code=obj[A][B]['product_code'].lower()
		if'integ'in vendor and'jnior'in product_code:meta.global_metadata.manufacturer=Manufacturer.INTEG;meta.global_metadata.product='JNIOR';meta.global_metadata.version=product_code.split(' ')[1];meta.device_type=Type.CINEMA