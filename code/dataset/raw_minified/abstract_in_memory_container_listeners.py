from muntjac.test.server.component.abstract_listener_methods_test import AbstractListenerMethodsTest as A
from muntjac.data.util.indexed_container import IndexedContainer as B
from muntjac.data.container import IItemSetChangeEvent as C,IItemSetChangeListener as D
class E(A):
	def testItemSetChangeListenerAddGetRemove(A):A._testListenerAddGetRemove(B,C,D)