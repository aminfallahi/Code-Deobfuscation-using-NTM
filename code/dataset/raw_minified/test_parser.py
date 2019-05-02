from unittest import TestCase as A
from ..parser import get_all_entries as B
from .utils import get_test_rss_path as C
class D(A):
	def setUp(A):A.test_file_path=C();A.entries=B('file://{}'.format(A.test_file_path))
	def test_entries(A):' Make sure we can parse RSS entries ';A.assertEqual(len(A.entries),25)