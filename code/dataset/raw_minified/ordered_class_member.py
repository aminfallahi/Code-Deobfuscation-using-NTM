E=type
import collections as A
class B(E):
	@classmethod
	def __prepare__(B,name,bases):return A.OrderedDict()
	def __new__(F,name,bases,classdict):
		I='__qualname__';H='__module__';C=bases;B='__ordered__';A=classdict;A[B]=[B for B in A.keys()if B not in(H,I)]
		for D in C:G=getattr(D,B,D.__dict__);A[B]=[A for A in G if A not in(H,I)]+A[B]
		return E.__new__(F,name,C,A)