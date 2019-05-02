G=None
from shutil import copyfileobj as C
from functools import partial as A
from contextlib import closing as D
import pkg_resources as B
E='twitterwrapper'
F=A(B.resource_stream,E)
def H(filename,to_filename=G):
	B=filename;A=to_filename
	if A is G:A=B
	with D(F('defaults/%s'%B))as E:
		with open(A,'w')as H:C(E,H)