from unittest import TestCase as A
import mock
from six import StringIO as B
from grab.util.warning import warn
class C(A):
	def test_warn(C):
		A=B()
		with mock.patch('sys.stderr',A):warn('abc')
		C.assertTrue('GrabDeprecationWarning: abc'in A.getvalue())