from unittest import TestCase as A
from ..api import file_validator as B,select_runnable as C
class D(A):
	def test_decorator_adds_runnable_name_to_wrapped_func(A):
		F='tagged'
		def D():0
		E=C(F)(B(D));A.assertEqual(E.runnable,F)