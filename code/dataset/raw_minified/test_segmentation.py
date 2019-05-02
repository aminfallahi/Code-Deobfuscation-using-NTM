import mahotas.segmentation,numpy as A,mahotas
from .utils import luispedro_jpg as D
def B():A=D();B,C=mahotas.segmentation.slic(A);assert B.shape==(A.shape[0],A.shape[1]);assert B.max()==C;F,E=mahotas.segmentation.slic(A,128);assert E<C