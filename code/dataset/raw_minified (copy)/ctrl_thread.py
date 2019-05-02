C=32
A=128
D=8
def B():
	F=CoramMemory(0,C,A,D,True);E=CoramChannel(0,32);B=0;sum=0
	for G in range(4):F.write(0,B,A);E.write(B);sum=E.read();B+=A*D*(C/8)
	print('sum=',sum)
B()