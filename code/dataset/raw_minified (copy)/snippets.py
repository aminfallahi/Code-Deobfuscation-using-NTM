C=float
B=int
def A(ms):'Returns an Integer approximated value';return B(ms/1000)
def D(sec):
	'Returns an Integer approximated value';A=sec
	if isinstance(A,C):return C(A*1000)
	return B(A*1000)