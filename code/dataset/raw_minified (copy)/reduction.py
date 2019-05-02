from numba.six.moves import reduce as C
def A(func):
	A=None
	def B(seq,res=A,init=0):
		B=C(func,seq,init)
		if res is not A:res[0]=B;return A
		else:return B
	return B
B=A