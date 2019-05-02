import unittest as A
from lib import mod1
class B(A.TestCase):
	def test1(A):A.assertEqual(mod1.covered_func(),9)