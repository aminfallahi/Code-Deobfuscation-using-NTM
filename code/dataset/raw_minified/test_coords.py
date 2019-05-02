E=round
D=tuple
C='tests/data/RGB.byte.tif'
import rasterio as B
def A():
	with B.open(C)as A:assert A.bounds==(101985.0,2611485.0,339315.0,2826915.0)
def F():
	with B.open(C)as A:assert A.ul(0,0)==(101985.0,2826915.0);assert A.ul(1,0)==(101985.0,2826614.95821727);assert A.ul(A.height,A.width)==(339315.0,2611485.0);assert D((E(B,6)for B in A.ul(~0,~0)))==(339014.962073,2611785.041783)
def G():
	with B.open(C)as A:assert D((E(B,6)for B in A.res))==(300.037927,300.041783)