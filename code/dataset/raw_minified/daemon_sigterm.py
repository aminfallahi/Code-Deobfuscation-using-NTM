from sys import argv
from time import sleep
from daemonize import Daemonize as A
B=argv[1]
def C():
	while True:sleep(5)
D=A(app='test_app',pid=B,action=C)
D.start()