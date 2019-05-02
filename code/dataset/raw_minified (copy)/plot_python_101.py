'\nBasic numerics and plotting with Python\n========================================\n\n'
import numpy as A
B=A.linspace(1,10,2000)
import pylab as C
C.plot(B,A.cos(B))