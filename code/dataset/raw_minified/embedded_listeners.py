from muntjac.test.server.component.abstract_listener_methods_test import AbstractListenerMethodsTest as A
from muntjac.ui.embedded import Embedded as B
from muntjac.event.mouse_events import ClickEvent as C,IClickListener as D
class E(A):
	def testClickListenerAddGetRemove(A):A._testListenerAddGetRemove(B,C,D)