import numpy as B,mahotas as C,sys
def A():E=True;A=B.zeros((64,64),bool);A[16:48,16:48]=E;D=B.logical_xor(A,C.erode(C.erode(A)));assert B.all(C.close_holes(D)==A);D[(12,12)]=E;A[(12,12)]=E;assert B.all(C.close_holes(D)==A);assert sys.getrefcount(D)==2