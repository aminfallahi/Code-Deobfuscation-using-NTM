D=2**4
E=2**10
A=32
B=CoramInStream(idx=0,datawidth=A*2,size=E)
C=CoramChannel(idx=0,datawidth=A,size=D)
def F():D=C.read();B.write_nonblocking(D,2);E=C.read();B.write_nonblocking(D+A*4/8,E-1)
while True:F()