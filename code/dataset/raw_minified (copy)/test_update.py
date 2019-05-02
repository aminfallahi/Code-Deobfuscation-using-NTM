D='werckercli.commands.update.puts'
import mock as A
from werckercli.tests import TestCase as C
from werckercli.commands import update as B
class E(C):
	LOW_VERSION='0.0.1';HIGH_VERSION='999.999.999'
	@A.patch(D,A.Mock())
	def test_newer_version(self):self.assertTrue(B.update(self.LOW_VERSION))
	@A.patch(D,A.Mock())
	def test_not_newer_version(self):self.assertFalse(B.update(self.HIGH_VERSION))