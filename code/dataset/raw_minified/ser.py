D=isinstance
import json as B
from json import dumps as E,loads
from BroControl import node
from BroControl import cmdresult as C
class A(B.JSONEncoder):
	def default(E,obj):
		A=obj
		if D(A,node.Node):return A.to_dict()
		if D(A,C.CmdResult):return A.to_dict()
		return B.JSONEncoder.default(E,A)
def F(obj):return B.dumps(obj,cls=A)