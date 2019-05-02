B=''
def A(given_bytes):return B.join(['%02X '%ord(A)for A in given_bytes]).strip()
def C(given_hex):
	A=given_hex;A=B.join(A.split());C=[]
	for D in range(0,len(A),2):C.append(chr(int(A[D:D+2],16)))
	return B.join(C)