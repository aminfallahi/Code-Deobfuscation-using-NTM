C=print
def A():
	C('thread 1');D=CoramMemory(0,32,128);B=CoramChannel(0,32);A=2048;sum=0
	for E in range(4):D.write(0,A,128);B.write(A);sum=B.read();A+=512
	C('thread1 sum=',sum)
A()