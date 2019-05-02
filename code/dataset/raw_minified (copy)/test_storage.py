D=None
import unittest as A
from aiorest_ws.storages.backends import BaseStorageBackend as B
class C(A.TestCase):
	def setUp(A):super(C,A).setUp();A.backend=B()
	def test_get(A):A.assertEqual(A.backend.get(),D)
	def test_save(A):A.assertEqual(A.backend.save(),D)