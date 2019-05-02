from django.test import TestCase as A
from schedule.models import Rule
class B(A):
	def setUp(A):0
	def test_get_params(A):B=Rule(params='count:1;bysecond:1;byminute:1,2,4,5');C={'count':1,'byminute':[1,2,4,5],'bysecond':1};A.assertEqual(B.get_params(),C)