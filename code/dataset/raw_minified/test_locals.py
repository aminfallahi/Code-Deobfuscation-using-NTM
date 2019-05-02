from __future__ import print_function,division,absolute_import
from numba import compiler as C,float32 as A
from numba import unittest_support as B
def D():A=123;return A
class E(B.TestCase):
	def test_seed_types(B):E=C.compile_isolated(D,(),locals={'x':A});B.assertEqual(E.signature.return_type,A)
if __name__=='__main__':B.main()