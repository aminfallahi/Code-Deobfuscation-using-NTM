def A():
	from doctest import testfile as C;import os;D='../doc';A=0;E=0
	for (F,K,G) in os.walk(D):
		for B in G:
			if B.endswith('.rst'):H=os.path.join(F,B);I,J=C(H);A+=I;E+=J
	assert A==0