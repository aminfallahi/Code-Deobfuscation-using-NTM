from sys import argv as A
from daemonize import Daemonize as B
C=A[1]
D=A[2]
E=A[3]
def F():
	with open(E,'w')as A:A.write('test')
G=B(app='test_app',pid=C,action=F,chdir=D)
G.start()