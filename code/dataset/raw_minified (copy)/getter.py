H=len
B=print
import rabbitpy as D
E='amqp://guest:guest@localhost:5672/%2F'
F=D.Connection(E)
G=F.channel()
C=D.Queue(G,'example')
while H(C)>0:A=C.get();B('Message:');B(' ID: %s'%A.properties['message_id']);B(' Time: %s'%A.properties['timestamp'].isoformat());B(' Body: %s'%A.body);A.ack();B('There are %i more messages in the queue'%H(C))