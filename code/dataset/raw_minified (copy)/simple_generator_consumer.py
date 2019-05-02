import logging as A
from amqpstorm import Connection as C
A.basicConfig(level=A.DEBUG)
def B():
	F='simple_queue';E='guest'
	with C('127.0.0.1',E,E)as D:
		with D.channel()as A:
			A.queue.declare(F);A.basic.consume(queue=F,no_ack=False)
			for B in A.build_inbound_messages():print(B.body);B.ack()
if __name__=='__main__':B()