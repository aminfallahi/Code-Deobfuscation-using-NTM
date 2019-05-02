import numpy as B,matplotlib.pyplot as A
from mpldatacursor import datacursor as C
F,D=A.subplots()
E=D.contour(B.random.random((10,10)))
C(E)
A.show()