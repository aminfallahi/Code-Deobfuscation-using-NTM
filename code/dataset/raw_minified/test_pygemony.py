from mock import patch
import unittest as A
from pyg.Pygemony import Pygemony as B
class C(A.TestCase):
	def test_hashing_pass(A):C=B.hash_todo('# TODO(ian): Testing 123','test.py');A.assertEqual(C,'8f83bdfe5ce85ac91d3e84e879fce24e')