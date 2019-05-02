from nose.tools import eq_
from standup.tests import BaseTestCase as A
class B(A):
	def test_help_view(A):B=A.client.get('/help');eq_(B.status_code,200)