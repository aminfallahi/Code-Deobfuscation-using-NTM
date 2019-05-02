from __future__ import print_function,absolute_import
E=getattr
import numpy as C
from numba import types as A
from numba import unittest_support as B
class D(B.TestCase):
	def test_numpy_integers(D):B=E(A,'int%d'%(C.dtype('int').itemsize*8));D.assertEqual(A.int_,B);B=E(A,'uint%d'%(C.dtype('uint').itemsize*8));D.assertEqual(A.uint,B)
if __name__=='__main__':B.main()