def A(iterator,size):
	A=[]
	for B in iterator:
		A.append(B)
		if len(A)==size:(yield A);del A[:]
	(yield A)