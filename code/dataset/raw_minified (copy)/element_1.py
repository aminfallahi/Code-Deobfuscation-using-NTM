from twisted.web.template import Element as B,renderer as A,XMLFile as C
from twisted.python.filepath import FilePath as D
class E(B):
	loader=C(D('template-1.xml'))
	@A
	def header(self,request,tag):return tag('Header.')
	@A
	def footer(self,request,tag):return tag('Footer.')