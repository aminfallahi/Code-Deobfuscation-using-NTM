from __future__ import print_function
D=print
def A():D('Hello world!')
def B(obj,spec):D('Custom help text.')
if __name__=='__main__':import sys;from marrow.script import Parser as C;sys.exit(C(A,help=B)(sys.argv[1:]))