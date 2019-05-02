import sys
def A(args=None):
	A=args;import pytest as B
	if not A:A=[]
	if not any((B for B in A[1:]if not B.startswith('-'))):A.append('tests');A.append('mocket')
	sys.exit(B.main(A))
if __name__=='__main__':A(sys.argv)