B=hasattr
import unittest as A
from mock import Mock
from contextio.lib.resources.discovery import Discovery as C
class D(A.TestCase):
	def setUp(A):A.discovery=C(Mock(),{})
	def test_constructor_creates_discovery_object_with_all_attributes_in_keys_list(A):A.assertTrue(B(A.discovery,'email'));A.assertTrue(B(A.discovery,'found'));A.assertTrue(B(A.discovery,'type'));A.assertTrue(B(A.discovery,'imap'));A.assertTrue(B(A.discovery,'documentation'))