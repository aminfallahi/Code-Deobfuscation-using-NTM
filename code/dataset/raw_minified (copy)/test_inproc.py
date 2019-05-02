import mock
from dccautomation import compat as B,common as C,inproc as A
class D(B.unittest.TestCase):
	def test_default(B):B.assertEqual(A.get_default_port(),A.DEFAULT_INPROC_PORT)
	def test_non_default(B):
		with mock.patch('os.environ',{C.ENV_INPROC_PORT:'20'}):B.assertEqual(A.get_default_port(),20)