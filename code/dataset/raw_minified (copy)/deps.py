from __future__ import absolute_import
import imp
def A(module):
	try:return __import__(module)
	except ImportError:return None
B=A('psutil')
C=A('thrift')
D=A('daemonize')