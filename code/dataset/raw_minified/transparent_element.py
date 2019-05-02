from twisted.web.template import Element as B,renderer as A,XMLFile as C
from twisted.python.filepath import FilePath as D
class E(B):
	loader=C(D('transparent-1.xml'))
	@A
	def renderer1(self,request,tag):return tag('hello')
	@A
	def renderer2(self,request,tag):return tag('world')