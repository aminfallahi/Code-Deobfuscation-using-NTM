import zmq
from llvm.core import Module
from llvm.ee import ExecutionEngine
from numpush.zmq_net import numsend as B
import bitey
C=bitey.load_library('./example')
D=zmq.Context.instance()
A=D.socket(zmq.PUSH)
A.bind('tcp://127.0.0.1:5555')
B(A,C)