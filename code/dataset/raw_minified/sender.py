import zmqpy as B
def A():
	C=B.Context();A=C.socket(B.PUSH);A.bind('tcp://*:3333');D='aaaaaaaaaa'
	for E in range(10000000):A.send(D,0)
	A.close();C.term()
if __name__=='__main__':A()