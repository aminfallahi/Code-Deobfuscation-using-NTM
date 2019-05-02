D='TestService'
from unittest import TestCase as A
from vyked import TCPService as B
class C(B):
	def __init__(A,port):super().__init__(D,1,host_port=port)
class E(A):
	def setUp(A):A._test_service=C(4500)
	def test_service_identifier(A):A.assertEquals(A._test_service.name,D.lower());A.assertEquals(A._test_service.version,str(1))