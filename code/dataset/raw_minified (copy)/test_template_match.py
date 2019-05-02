import numpy as A,mahotas.convolve
from mahotas.convolve import template_match as G
def B():
	A.random.seed(33);C=255*A.random.random((1024,512));F=C[8:12,8:12]+1;B=G(C,F);assert B[(10,10)]==16
	for H in range(100):D=A.random.randint(B.shape[0]-4);E=A.random.randint(B.shape[1]-4);assert A.allclose(B[(D+2,E+2)],A.sum((C[D:D+4,E:E+4]-F)**2))