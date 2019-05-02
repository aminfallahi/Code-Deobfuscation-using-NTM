import os
from os.path import join as A
from twisted.trial import unittest as B
from twisted.python import util
class C(B.TestCase):
	def testNoSlashSlashComments(B):C=util.sibpath(__file__,A(os.pardir,'protocols','_c_urlarg.c'));D=file(C).read();B.assertEquals(D.find('//'),-1)