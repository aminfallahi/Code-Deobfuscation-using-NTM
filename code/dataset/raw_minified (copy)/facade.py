A=None
import puremvc.patterns.command
class B(puremvc.patterns.command.SimpleCommand):
	def execute(B,note):A=note.getBody();A.result=2*A.input
class C:
	input=A;result=A
	def __init__(A,input):A.input=input