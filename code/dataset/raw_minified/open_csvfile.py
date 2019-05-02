def A(filename,delimiter=','):
	with open(filename,'r')as B:A=B.read().split('\n')
	for (C,D) in enumerate(A):A[C]=D.split(delimiter)
	return A