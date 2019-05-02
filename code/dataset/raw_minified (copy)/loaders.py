import unittest as B
from wsgid.loaders import import_object as A
class C(B.TestCase):
	def test_import_existing_object(B):C=A('os.path.join');from os.path import join as D;B.assertEquals(C,D)
	def test_import_non_existing_object(B):B.assertRaises(Exception,A,'os.path.joinnames')