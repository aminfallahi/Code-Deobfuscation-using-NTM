from muntjac.test.server.component.abstract_listener_methods_test import AbstractListenerMethodsTest as A
from muntjac.ui.horizontal_split_panel import HorizontalSplitPanel as B
from muntjac.ui.abstract_split_panel import SplitterClickEvent as C,ISplitterClickListener as D
class E(A):
	def testSplitterClickListenerAddGetRemove(A):A._testListenerAddGetRemove(B,C,D)