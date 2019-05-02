C=print
import sys
A=sys.argv[1]
if A.startswith('http'):C(A)
else:B=float(A)+0.1;C('Django>=%s,<%.1f'%(A,B))