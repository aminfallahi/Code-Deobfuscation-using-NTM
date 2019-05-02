from nose.tools import eq_
from js_helper import skip_on_acorn as A,TestCase as B
class C(B):
	@A
	def test__proto__asignment(self):"\n        Make sure that setting __proto__ doesn't traceback.\n        ";A=self;A.setUp();A.run_script("\n            var obj = {foo: 'bar', __proto__: null};\n        ");A.assert_silent()