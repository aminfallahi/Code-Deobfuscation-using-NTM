F='utf-8'
E=list
B=isinstance
def C(arg):
	A=arg
	if B(A,E):return[C(B)for B in A]
	else:return A.encode(F)
def D(arg):
	A=arg
	if B(A,E):return[D(B)for B in A]
	else:return A.decode(F)if B(A,str)else A