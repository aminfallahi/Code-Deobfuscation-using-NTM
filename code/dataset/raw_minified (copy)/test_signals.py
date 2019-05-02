from django.test import TestCase as A
from nose.tools import ok_
from users.test.factories import UserFactory as B
class C(A):
	def setUp(A):A.user=B()
	def test_new_users_get_auth_token(A):ok_(A.user.auth_token)