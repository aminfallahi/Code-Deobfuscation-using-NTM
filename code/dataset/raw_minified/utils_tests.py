try:import unittest2 as B
except ImportError:import unittest as B
from pika import utils as A
class C(B.TestCase):
	def test_is_callable_true(B):B.assertTrue(A.is_callable(A.is_callable))
	def test_is_callable_false(B):B.assertFalse(A.is_callable(1))