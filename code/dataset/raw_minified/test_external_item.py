try:from unittest.mock import MagicMock as B
except ImportError:from mock import MagicMock as B
from base_test_case import BaseTestCase as A
from cursesmenu import CursesMenu
from cursesmenu.items import ExternalItem as C
class D(A):
	def setUp(A):super(D,A).setUp();A.mock_set_up=B();A.mock_action=B(return_value=0);A.mock_clean_up=B();C.set_up=A.mock_set_up;C.clean_up=A.mock_clean_up;C.action=A.mock_action