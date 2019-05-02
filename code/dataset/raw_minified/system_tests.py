import sys,django as A
from django.test import TestCase as B
class C(B):
	def test_django_version(B):B.assert_(A.get_version()>='1.2.1')
	def test_python_version(A):A.assert_(sys.version_info[0:3]>=(2,6,5))