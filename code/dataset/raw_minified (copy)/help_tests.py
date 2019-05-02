import unittest as A,envoy
from csvfilter import VERSION as B
class C(A.TestCase):
	def setUp(A):A.r=envoy.run('csvfilter -h')
	def test_help_output(A):A.assertEqual(0,A.r.status_code)
	def test_version_is_present(A):A.assertTrue(B in A.r.std_out)