from __future__ import absolute_import
import sh,os
from .base import DjangoCookieTestCase as A
class B(A):
	def test_virtualenv_install(A):
		A.generate_project()
		try:os.chdir('wagtail_project');B=sh.Command('make');B('virtualenv')
		except sh.ErrorReturnCode as C:raise AssertionError(C)