import unittest as A
from chainpoint.run import db
from chainpoint.Receipt import Receipt as B
class C(A.TestCase):
	def setUp(A):db.create_all()
	def tearDown(A):db.session.remove();db.drop_all()
	def test_new_receipt(A):C='';D=B()