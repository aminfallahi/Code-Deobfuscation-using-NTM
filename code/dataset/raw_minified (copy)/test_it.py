from django.core.urlresolvers import reverse
from django.test import TestCase as A
from django.test.utils import setup_test_environment as B
B()
class C(A):
	def test_plate(A):B=A.client.get('/');A.assertEqual(B.status_code,200)