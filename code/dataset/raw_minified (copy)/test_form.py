from django.test import TestCase as A
from wall.forms import WallItemForm as B
class C(A):
	def setUp(A):A.form=B()
	def tearDown(A):0
	def test_display_form(A):B='<p><label for="id_posting">Item:</label> <textarea id="id_posting" rows="5" cols="50" name="posting"></textarea></p>';A.assertEquals(A.form.as_p(),B)