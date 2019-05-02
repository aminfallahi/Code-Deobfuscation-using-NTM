import os,inspect as B
def A(path):
	'return an absolute path from a given path which\n    is relative to the calling module';A=path
	if os.path.isabs(A):return A
	C=B.stack()[1][1];D=os.path.abspath(os.path.dirname(C));return os.path.join(D,A)