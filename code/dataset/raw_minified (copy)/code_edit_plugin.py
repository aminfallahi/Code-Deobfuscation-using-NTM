'\nThis module contains the CodeEdit designer plugin.\n'
from pyqode.core._designer_plugins import WidgetPlugin as A
from pyqode.core.api import CodeEdit as B
class C(A):
	'\n    Designer plugin for CodeEdit.\n    '
	def klass(A):return B
	def objectName(A):return'codeEdit'