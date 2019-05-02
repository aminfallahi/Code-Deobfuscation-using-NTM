C=ImportError
try:import unittest2 as A
except C:import unittest as A
try:from unittest import mock
except C:import mock
from qrcode import run_example as B
class D(A.TestCase):
	@mock.patch('PIL.Image.Image.show')
	def runTest(self,mock_show):B();mock_show.assert_called_with()