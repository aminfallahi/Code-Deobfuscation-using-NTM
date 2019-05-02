from pylearn2.utils import serial as F
import sys
N,G=sys.argv
B=F.load(G)
from pylearn2.gui.patch_viewer import make_viewer as H
C=B.generator.get_output_space()
I=C.get_total_dimension()
import numpy as J
D=1
E=int(J.sqrt(I/D))
from pylearn2.space import Conv2DSpace as K
L=K(shape=[E,E],num_channels=D,axes=('b',0,1,'c'))
A=C.format_as(batch=B.generator.sample(100),space=L).eval()
print(A.min(),A.mean(),A.max())
M=H(A*2.0-1.0)
M.show()