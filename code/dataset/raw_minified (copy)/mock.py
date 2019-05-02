C='message'
A=None
from ..core import Observable as B
class D(B):
	def __init__(A):B.__init__(A)
	def subscribe(A,channel,callback=A,error=A,connect=A,reconnect=A,disconnect=A):A.on(C,callback)
	def unsubscribe(A,channel):0
	def receive_message(A,message):A.emit(C,message)