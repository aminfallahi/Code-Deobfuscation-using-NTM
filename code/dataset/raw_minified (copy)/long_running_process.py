from __future__ import print_function,unicode_literals
A=print
import time,sys,os
def B():
	A('This is LRP',os.getpid());A('OK');sys.stdout.flush()
	for B in range(20):time.sleep(1)
	A('LRP is done now');sys.stdout.flush()
if __name__=='__main__':B()