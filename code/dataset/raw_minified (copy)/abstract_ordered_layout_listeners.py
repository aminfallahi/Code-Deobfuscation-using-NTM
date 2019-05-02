from muntjac.test.server.component.abstract_listener_methods_test import AbstractListenerMethodsTest as A
from muntjac.ui.vertical_layout import VerticalLayout as B
from muntjac.event.layout_events import LayoutClickEvent as C,ILayoutClickListener as D
class E(A):
	def testLayoutClickListenerAddGetRemove(A):A._testListenerAddGetRemove(B,C,D)