G=len
import unittest as A
from pynes.compiler import lexical as D,syntax as E,semantic as F
class B(A.TestCase):
	def test_tax_sngl(A):I='type';B=list(D('TAX'));A.assertEquals(1,G(B));A.assertEquals('T_INSTRUCTION',B[0][I]);C=E(B);A.assertEquals(1,G(C));A.assertEquals('S_IMPLIED',C[0][I]);H=F(C);A.assertEquals(H,[170])