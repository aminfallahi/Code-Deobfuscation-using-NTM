from circus.tests.test_command_incrproc import FakeArbiter as D
from circus.tests.support import TestCircus as A,EasyTestSuite as B
from circus.commands.quit import Quit
class C(A):
	def test_quit(B):C=Quit();A=D();B.assertTrue(A.watchers[0].numprocesses,1);E=C.message('dummy')['properties'];C.execute(A,E);B.assertEqual(len(A.watchers),0)
E=B(__name__)