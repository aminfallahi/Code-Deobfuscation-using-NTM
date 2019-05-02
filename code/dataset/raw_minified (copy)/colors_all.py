from __future__ import print_function
import sys,os
sys.path.insert(0,os.path.abspath('..'))
from clint.textui import colored as A
C='THIS TEXT IS COLORED %s!'
if __name__=='__main__':
	for B in A.COLORS:print(getattr(A,B)(C%B.upper()))