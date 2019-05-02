import os,unittest as B
from utils.process import pid_exists as A
class C(B.TestCase):
	def test_my_own_pid(B):C=os.getpid();B.assertTrue(A(C))
	def test_inexistant_pid(C):
		for B in xrange(30000):
			if not A(B):return
		raise Exception('Probably a bug in pid_exists or more than 30000 procs!!')