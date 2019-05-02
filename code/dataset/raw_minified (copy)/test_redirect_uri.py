from django.test import TestCase as A
from doac.models import Client as C,RedirectUri as D
class B(A):
	def test_unicode(E):B=C(name='Test Client',access_host='http://localhost/');B.save();A=D(client=B,url='http://localhost/redirect_endpoint');A.save();E.assertEqual(unicode(A),A.url)