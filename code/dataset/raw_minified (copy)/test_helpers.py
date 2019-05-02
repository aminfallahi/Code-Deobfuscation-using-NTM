from django.test import TestCase as B
from periods import helpers as A
class C(B):
	def test_http(B):C=A.get_full_domain();B.assertEqual('http://example.com',C)
	def test_https(B):
		with B.settings(SECURE_SSL_REDIRECT=True):C=A.get_full_domain();B.assertEqual('https://example.com',C)