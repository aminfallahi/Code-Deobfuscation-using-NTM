import DeepFried2 as A
class B(A.Module):
	def __init__(B,shape,init=A.init.const(0),bcast=None):C=shape;A.Module.__init__(B);B.b=B._addparam(C,init,name='b_{}'.format(C),broadcastable=bcast,decay=False)
	def symb_forward(A,symb_input):return symb_input+A.b.param