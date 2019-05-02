import sys,zmq
from types import ModuleType as B
from numpush.zmq_net import numrecv as C
D=zmq.Context.instance()
A=D.socket(zmq.PULL)
A.connect('tcp://127.0.0.1:5555')
E=C(A)
assert type(E)is B
assert'example'in sys.modules
import example as F
assert F.test(1,2)==3