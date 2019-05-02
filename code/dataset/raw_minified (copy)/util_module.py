from unittest import TestCase as B
from grab.util.module import import_string as A,ImportStringError as C
class D(B):
	def test_import_string(B):C=A('test.case.util_module');B.assertTrue(hasattr(C,'UtilModuleTestCase'))
	def test_import_string_error(B):B.assertRaises(C,A,'test.case.zzzzzzzzzzzz')