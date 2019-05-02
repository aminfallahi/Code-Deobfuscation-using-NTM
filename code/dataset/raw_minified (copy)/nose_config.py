from nose.plugins.base import Plugin as A
from tiget.plugins import load_plugin as B
class C(A):
	def options(A,parser,env):0
	def configure(A,options,conf):B('tiget.core')