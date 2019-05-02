from __future__ import absolute_import
from freight.testutils import TestCase as A
class B(A):
	def test_simple(B):
		C='/api/0/not-a-real-endpoint'
		for D in ('get','post','put','delete','patch'):A=getattr(B.client,D)(C);assert A.status_code==404;assert ''.join(A.data.splitlines())=='{"error": "Not Found"}'