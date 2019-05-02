from base_test_case import BaseTestCase as A
from cursesmenu import CursesMenu as B
from cursesmenu.items import SelectionItem as D
class C(A):
	def setUp(A):super(C,A).setUp();A.menu=B('self.menu','TestSelectionItem')
	def test_init(A):F='selection_item_2';E='selection_item_1';B=D(E,1,A.menu);C=D(text=F,index=2,menu=A.menu);A.assertEqual(B.text,E);A.assertEqual(C.text,F);A.assertEqual(B.menu,A.menu);A.assertEqual(C.menu,A.menu);A.assertTrue(B.should_exit);A.assertTrue(C.should_exit)