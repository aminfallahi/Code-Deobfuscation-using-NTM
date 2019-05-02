from __future__ import absolute_import
from sys import platform as A
def B():
	if'linux'in A:from pytify.linux import Linux;return Linux
	elif'darwin'in A:from pytify.darwin import Darwin as B;return B
	else:raise Exception('%s is not supported.'%A)