from js_helper import TestCase as A
class B(A):
	def test_double_escaped(A):"Test that escaped characters don't result in errors.";A.run_script('\n        var x = "ሴ\x12"\n        var y = "\\u1234\\x12"\n        ');A.assert_silent()