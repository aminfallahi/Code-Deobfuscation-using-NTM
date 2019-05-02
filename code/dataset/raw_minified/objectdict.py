class A(dict):
	' A dict subclass which allows access by named attribute.\n\n    ';__slots__=()
	def __getattr__(A,attr):
		B=attr
		if B in A:return A[B]
		C="'%s' object has no attribute '%s'";raise AttributeError(C%(type(A).__name__,B))