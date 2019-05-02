from circus.consumer import CircusConsumer as A
from zmq.green import Context as B,Poller as C,POLLIN as D
class E(A):
	def _init_context(A,context):A.context=context or B()
	def _init_poller(A):A.poller=C();A.poller.register(A.pubsub_socket,D)