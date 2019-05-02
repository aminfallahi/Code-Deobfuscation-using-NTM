'\nThis example demonstrates both draggable annotation boxes and using the\n``display="multiple"`` option.\n'
F=range
import matplotlib.pyplot as A,numpy as C
from mpldatacursor import datacursor as D
E=C.outer(F(10),F(1,5))
G,B=A.subplots()
B.set_title('Try dragging the annotation boxes')
B.plot(E)
D(display='multiple',draggable=True)
A.show()