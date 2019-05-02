from __future__ import unicode_literals
E=len
from unittest import TestCase as A
from ..misc import readable_random_token as B
class C(A):
	def test_random_token(A):D=True;C=B();F=B();A.assertNotEqual(C,F);A.assertTrue('-'in C);A.assertFalse(' 'in C);A.assertTrue(' - 'in B(add_spaces=D));A.assertFalse('1'in B(alphanumeric=D));A.assertEqual(E(C),19);A.assertEqual(E(B(short_token=D)),9);A.assertEqual(E(B(long_token=D)),39)