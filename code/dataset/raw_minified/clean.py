from __future__ import print_function,unicode_literals
import os.path
from pre_commit.util import rmtree as B
def A(runner):
	A=runner
	if os.path.exists(A.store.directory):B(A.store.directory);print('Cleaned {0}.'.format(A.store.directory))
	return 0