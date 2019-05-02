from ee.utils import test
from ee.cli.main import get_test_app as B
class A(test.EETestCase):
	def test_ee_cli(A):A.app.setup();A.app.run();A.app.close()
	def test_ee_cli_show_edit(A):A.app=B(argv=['site','show','example1.com']);A.app.setup();A.app.run();A.app.close()