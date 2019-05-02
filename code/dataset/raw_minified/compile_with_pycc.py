from numba import exportmany as B,export as C
def A(a,b):return a*b
C('multi i4(i4, i4)')(A)
B(['multf f4(f4, f4)','mult f8(f8, f8)'])(A)