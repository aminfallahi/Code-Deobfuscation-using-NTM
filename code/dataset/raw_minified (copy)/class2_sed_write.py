import numpy as B
from hyperion.model import ModelOutput as C
from hyperion.util.constants import pc
D=C('class2_sed.rtout')
A=D.get_sed(inclination=0,aperture=-1,distance=300*pc)
B.savetxt('sed.txt',list(zip(A.wav,A.val)),fmt='%11.4e %11.4e')