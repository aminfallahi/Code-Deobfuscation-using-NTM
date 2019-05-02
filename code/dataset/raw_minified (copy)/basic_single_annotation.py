'An example demonstrating displaying only a single annotation box cursor for\nmultiple subplots.'
D=range
import matplotlib.pyplot as A,numpy as B
from mpldatacursor import datacursor as C
A.figure()
A.subplot(2,1,1)
A.title('Note that only one cursor will be displayed for display="single"')
A.plot(D(10),'ro-')
A.subplot(2,1,2)
E=B.arange(100).reshape((10,10))
A.plot(D(10),'bo')
C(display='single')
A.show()