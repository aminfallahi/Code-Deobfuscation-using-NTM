from olympia.amo.tests import TestCase as A
class B(A):
	def test_for_security_headers(B):'Test that security headers are set.';A=B.client.get('/en-US/firefox/');assert A.status_code==200;assert A['x-xss-protection']=='1; mode=block';assert A['x-content-type-options']=='nosniff';assert A['x-frame-options']=='DENY'