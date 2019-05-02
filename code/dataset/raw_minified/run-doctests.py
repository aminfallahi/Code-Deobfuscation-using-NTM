import doctest as D,sys,unittest_expander as E
if __name__=='__main__':
	A,B=D.testmod(E);C='Test summary: {1}/{0} passed and {2}/{0} failed.'.format(B,B-A,A)
	if A:sys.exit(C)
	else:print(C)