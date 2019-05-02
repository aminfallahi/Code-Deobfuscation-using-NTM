from muntjac.api import VerticalLayout as A,Embedded as B
from muntjac.terminal.external_resource import ExternalResource as D
class E(A):
	def __init__(C):super(E,C).__init__();A=B('Google Search',D('http://www.google.com'));A.setType(B.TYPE_BROWSER);A.setWidth('100%');A.setHeight('400px');C.addComponent(A)