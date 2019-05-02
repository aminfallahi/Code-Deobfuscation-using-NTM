from operator import lt,gt
def A(left,right):A=D(left,lt);B=D(right,gt);return max((C-D for(C,D)in zip(A,B)))+1
def D(tree,comp,level=0,cont=None):
	C=level;B=tree;A=cont
	if not A:A=[B.x]
	elif len(A)<C+1:A.append(B.x)
	elif comp(A[C],B.x):A[C]=B.x
	for E in B.children:D(E,comp,C+1,A)
	return A