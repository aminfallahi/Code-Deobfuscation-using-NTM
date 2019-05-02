from django.test import TestCase as B
from constance import settings as A
from tests.storage import StorageTestsMixin as C
class D(C,B):
	def setUp(B):super(D,B).setUp();B.old_backend=A.BACKEND;A.BACKEND='constance.backends.database.DatabaseBackend'
	def tearDown(B):A.BACKEND=B.old_backend