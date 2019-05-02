C=True
B=False
from nose2.compat import unittest as A
class D(A.TestCase):
	@A.expectedFailure
	def test_should_fail(self):assert B
	@A.expectedFailure
	def test_should_pass(self):assert C
	def test_whatever(A):assert C
	def test_fails(A):assert B