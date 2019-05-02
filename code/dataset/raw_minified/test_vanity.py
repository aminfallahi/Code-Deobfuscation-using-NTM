C='location'
B=False
from nose.tools import eq_
from kitsune.sumo.tests import TestCase as A
class D(A):
	"We're just asserting that these vanity URLs go somewhere."
	def test_windows7(D):A=D.client.get('/en-US/windows7-support',follow=B);eq_(302,A.status_code);assert'home'in A[C]
	def test_contribute(D):A=D.client.get('/en-US/contribute',follow=B);eq_(302,A.status_code);assert'get-involved'in A[C]