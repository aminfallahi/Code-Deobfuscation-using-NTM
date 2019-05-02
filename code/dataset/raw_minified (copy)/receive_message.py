import toto
from toto.invocation import *
from tornado.ioloop import IOLoop
@asynchronous
def invoke(handler,params):
	A='message'
	def receive_message(message):handler.respond(result={A:message})
	handler.register_event_handler(A,receive_message,deregister_on_finish=True)