class A(dict):
	def set(A,key,value):A[key]=value
	def mget(C,keys):
		E=None;A=[]
		for D in keys:
			B=C.get(D,E)
			if B is not E:A.append(B)
		return A