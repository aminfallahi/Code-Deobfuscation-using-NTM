from circus.arbiter import Arbiter as A
from circus.green.controller import Controller as B
from zmq.green.eventloop import ioloop as C
from zmq.green import Context as D
class E(A):
	def _init_context(A,context):A.context=context or D.instance();A.loop=C.IOLoop.instance();A.ctrl=B(A.endpoint,A.multicast_endpoint,A.context,A.loop,A,A.check_delay)