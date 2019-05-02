'Tests for stevedore.example.simple\n'
from stevedore.example import simple as A
from stevedore.tests import utils
class B(utils.TestCase):
	def test_simple_items(B):C=A.Simple(100);D=''.join(C.format({'a':'A','b':'B'}));E='\n'.join(['a = A','b = B','']);B.assertEqual(D,E)