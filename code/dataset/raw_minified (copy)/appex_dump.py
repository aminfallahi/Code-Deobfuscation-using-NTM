import appex as A,inspect as C
def B():
	if A.is_running_extension():
		for D in C.getmembers(A):
			B,E=D
			if B.startswith('get_'):print('{:<11} : {}'.format(B.partition('_')[2],E()))
if __name__=='__main__':B()