from muntjac.test.server.component.abstract_listener_methods_test import AbstractListenerMethodsTest as A
from muntjac.ui.tab_sheet import TabSheet as B,SelectedTabChangeEvent as C,ISelectedTabChangeListener as D
class E(A):
	def testSelectedTabChangeListenerAddGetRemove(A):A._testListenerAddGetRemove(B,C,D)