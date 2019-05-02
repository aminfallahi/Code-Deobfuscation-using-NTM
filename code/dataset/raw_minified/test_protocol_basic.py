import unittest as A
from tempodb.protocol.protocol import make_series_key as B
class C(A.TestCase):
	def test_make_series_key(A):C='my-key';D=['foo'];E={'bar':'baz'};F=B(C,D,E);A.assertEquals(F,'{"attributes": {"bar": "baz"}, "key": "my-key", "tags": ["foo"]}')