D=open
C=print
import sys
input=D(sys.argv[1],'r')
A=D(sys.argv[2],'w')
for B in input:
	if B[0]=='>':C>>A,'@HTW-'+B[1:-1];continue
	else:C>>A,B[:-1];C>>A,'+';C>>A,'H'*len(B[:-1])
input.close()
A.close()