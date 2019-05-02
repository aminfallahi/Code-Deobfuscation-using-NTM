import unittest as A,manager as B
from BeautifulSoup import BeautifulSoup as C
class D(A.TestCase):
	def setUp(A):B.app.config['TESTING']=True;A.app=B.app.test_client()
	def test_index_returns_html(A):B=A.app.get('/');D=C(B.data);A.assertTrue(D.findAll('html'),'index page does not return html')
if __name__=='__main__':A.main()