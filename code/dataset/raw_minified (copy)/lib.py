E=type
def D(d1,d2):
	A=d1.copy()
	for (B,C) in d2.iteritems():
		if A.has_key(B):
			if E(A[B])is dict:A[B]=D(A[B],C)
			else:raise KeyError('Collision in key %s type %s'%(B,E(A[B])))
		else:A[B]=C
	return A