' Look for changes in numpy behavior over versions\n'
import numpy as A
def B():
	' Return True if ufuncs on memmap arrays always return memmap arrays\n\n    This should be True for numpy < 1.12, False otherwise.\n    '
	with open(__file__,'rb')as B:C=A.memmap(B,mode='r',shape=(10,),dtype=A.uint8);D=isinstance(C+1,A.memmap)
	return D
C=B()