import logging as A,settings
D=[(A.StreamHandler(),A.DEBUG)]
def B():
	E=A.Formatter('%(asctime)s [%(levelname)-8.8s] %(message)s');C=A.getLogger();C.setLevel(A.DEBUG)
	for (B,F) in D:B.setFormatter(E);B.setLevel(F);C.addHandler(B)