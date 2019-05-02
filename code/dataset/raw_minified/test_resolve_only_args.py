from ..resolve_only_args import resolve_only_args as B
def A():
	E=None
	def C(*B,**A):return A
	A={'one':1,'two':2};D=B(C);assert D(E,A,E)==A