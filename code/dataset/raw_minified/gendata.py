F=None
import random as A
def B(N,d,bounds,clsses,fname):
	D=bounds;E=open(fname,'w')
	for G in xrange(N):
		B=[F]*(d+1)
		for C in xrange(d):B[C]=A.uniform(D[C][0],D[C][1])
		B[d]=A.choice(clsses);E.write(', '.join(map(str,B))+'\n')
	E.close()
def C(d,bounds,clsses):
	D=bounds;B=[F]*(d+1)
	for C in xrange(d):B[C]=A.uniform(D[C][0],D[C][1])
	B[d]=A.choice(clsses);return B