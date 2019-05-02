from muntjac.test.server.component.abstract_listener_methods_test import AbstractListenerMethodsTest as A
from muntjac.ui.label import Label,ValueChangeEvent as B
from muntjac.data.property import IValueChangeListener as C
class D(A):
	def testValueChangeListenerAddGetRemove(A):A._testListenerAddGetRemove(Label,B,C)