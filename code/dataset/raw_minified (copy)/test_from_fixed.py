from agate import Table as D
from agate.testcase import AgateTestCase as A
class B(A):
	def test_from_fixed(A):B=D.from_csv('examples/testfixed_converted.csv');C=D.from_fixed('examples/testfixed','examples/testfixed_schema.csv');A.assertColumnNames(C,B.column_names);A.assertColumnTypes(C,[type(A)for A in B.column_types]);A.assertRows(C,B.rows)