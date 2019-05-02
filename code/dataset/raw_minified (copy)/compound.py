B=None
from telegrambot.bot_views.generic.base import TemplateCommandView as A
class C(A):
	list_view_class=B;detail_view_class=B
	@classmethod
	def as_command_view(A,**C):
		def B(bot,update,**E):
			B=update;C=B.message.text.split(' ')
			if len(C)>1:D=A.detail_view_class(C[1])
			else:D=A.list_view_class()
			return D.handle(bot,B,**E)
		return B