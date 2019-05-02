import shutilwhich
from shutil import which
import pytest as B
def A(name,scope='session',**A):
	@B.fixture(scope=scope,**A)
	def C():
		A=which(name)
		if not A:B.skip('Skipping test; missing binary: {}'.format(A))
		return A
	return C