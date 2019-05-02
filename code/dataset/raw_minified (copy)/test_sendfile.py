import socket as B,numpy as C,os.path as F
from tempfile import mkdtemp as G
from numpush.posix_io.sendfile import posix_sendfile as H
D=B.socket(B.AF_INET,B.SOCK_STREAM)
D.connect(('127.0.0.1',8000))
E=F.join(G(),'map')
A=C.linspace(0,1000)
I=open(E,'a+')
J=C.memmap(E,dtype=A.dtype,shape=A.shape)
J[:]=A[:]
K=H(D,I,nbytes=1024)
assert K==A.nbytes