import sys,os
def A():A=os.path.dirname(os.path.dirname(os.path.abspath(__file__)));sys.path.insert(0,A);import pip;return pip.main()
if __name__=='__main__':
	exit=A()
	if exit:sys.exit(exit)