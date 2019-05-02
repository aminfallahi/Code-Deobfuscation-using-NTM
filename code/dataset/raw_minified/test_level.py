import unittest as C
from vint.linting.level import Level as A,is_level_enabled as B
class D(C.TestCase):
	def test_is_level_enabled_with_same_level(C):C.assertTrue(B(A.WARNING,A.WARNING))
	def test_is_level_enabled_with_lower_level(C):C.assertFalse(B(A.WARNING,A.ERROR))
	def test_is_level_enabled_with_higher_level(C):C.assertTrue(B(A.ERROR,A.STYLE_PROBLEM))
if __name__=='__main__':C.main()