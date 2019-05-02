import unittest as B
from vint.ast.node_type import NodeType as A
class C(B.TestCase):
	def test_get_node_type_name(B):B.assertIs(A(1),A.TOPLEVEL);B.assertIs(A(89),A.REG)
if __name__=='__main__':B.main()