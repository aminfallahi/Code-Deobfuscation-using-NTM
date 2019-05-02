from .colls import walk_values as D
from .funcs import iffy
__all__='namespace',
class B(type):
	def __new__(C,name,bases,attrs):A=attrs;A=D(iffy(callable,staticmethod),A);return super(B,C).__new__(C,name,bases,A)
class A:__metaclass__=B