' hostlists plugin to get hosts from a file '
A='file'
import os
def B():return[A]
def C(value,name=A):
	B=[]
	for A in [A.strip()for A in open(os.path.expanduser(value),'r').readlines()]:
		if not A.startswith('#')and len(A.strip()):B.append(A)
	return B