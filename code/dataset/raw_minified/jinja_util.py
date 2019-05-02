from copy import copy
from six.moves import filter
C=frozenset(['selected','checked','compact','declare','defer','disabled','ismap','multiple','nohref','noresize','noshade','nowrap'])
def A(v):
	A=copy(v)
	for B in filter(lambda k:k in C,A.keys()):
		if A[B]:A[B]=B
		else:A[B]=None
	return A