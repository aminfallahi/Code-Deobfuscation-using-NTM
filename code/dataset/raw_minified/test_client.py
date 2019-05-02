D='http://example.com/stash/rest/api/1.0/admin/groups'
C='http://example.com/stash'
from unittest import TestCase as B
from stashy.client import StashClient as A
class E(B):
	def test_url_without_slash_prefix(B):E=A(C);B.assertEqual(D,E.url('api/1.0/admin/groups'))
	def test_url_with_slash_prefix(B):E=A(C);B.assertEqual(D,E.url('/api/1.0/admin/groups'))