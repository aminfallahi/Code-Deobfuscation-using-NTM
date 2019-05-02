'\nThis is obsoleted module. Use selection package instead.\n'
from selection.base import SelectorList,RexResultList
from selection.backend import PyquerySelector,XpathSelector as A
from grab.util.warning import warn
class B(A):
	def __init__(A,*C,**D):warn('You are using XpathSelector from deprecated `grab.selector` package. Please, switch to `selection` package.');super(B,A).__init__(*C,**D)