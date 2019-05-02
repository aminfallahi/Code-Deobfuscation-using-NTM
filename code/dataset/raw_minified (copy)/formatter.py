import unittest as A
class B(A.TestCase):
	def assertFormattedViolations(A,formatter,violations,expected_output):B=formatter.format_violations(violations);A.assertEqual(B,expected_output)