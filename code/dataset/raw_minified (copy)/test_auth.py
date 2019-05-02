from flask import Response as C
from cabu.tests.test_base import TestBase as A
from cabu.auth import check_auth as B,authenticate as D
class E(A):
	def test_check_auth(A):
		C='admin'
		with A.app.test_request_context():A.assertTrue(B(C,C));A.assertFalse(B(C,'nonadmin'))
	def test_authenticate(A):B=D();A.assertIsInstance(B,C);E,F=A.parse_response(B);A.assertEquals(401,401)