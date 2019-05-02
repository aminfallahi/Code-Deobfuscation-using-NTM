'\n\n'
import unittest as A,warnings as B
class C(A.TestCase):
	def test_insecure_setup(A):
		with B.catch_warnings(record=True)as C:from flask import Flask;from flask_limiter import Limiter as D;E=Flask(__name__);D(E);A.assertEqual(len(C),1)