from muntjac.test.server.component import abstract_listener_methods_test as A
from muntjac.data.util.propertyset_item import PropertysetItem as B
from muntjac.data.item import IPropertySetChangeEvent as C,IPropertySetChangeListener as D
class E(A.AbstractListenerMethodsTest):
	def testPropertySetChangeListenerAddGetRemove(A):A._testListenerAddGetRemove(B,C,D)