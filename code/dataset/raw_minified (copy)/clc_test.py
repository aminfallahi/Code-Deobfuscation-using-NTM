'\nCLC, Clear Carry\n\nThis is a test for the clear carry instruction\n'
C='CLC'
import unittest as A
from pynes.tests import MetaInstructionCase as B
class D(A.TestCase):__metaclass__=B;asm=C;lex=[('T_INSTRUCTION',C)];syn=['S_IMPLIED'];code=[24]