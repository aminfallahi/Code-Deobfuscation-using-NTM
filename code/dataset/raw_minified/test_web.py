import unittest as B
from .context import app as A
A.config['TWILIO_ACCOUNT_SID']='ACxxxxxx'
A.config['TWILIO_AUTH_TOKEN']='yyyyyyyyy'
A.config['TWILIO_CALLER_ID']='+15558675309'
A.config['TWILIO_APP_SID']='APzzzzzzzzzzzz'
class C(B.TestCase):
	def setUp(B):B.app=A.test_client()
class D(C):
	def test_index(A):B=A.app.get('/');A.assertEqual('200 OK',B.status)