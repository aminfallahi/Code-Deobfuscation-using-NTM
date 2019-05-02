import DeepFried2 as A
class B(A.Module):
	def __init__(B,scalar):A.Module.__init__(B);B.scalar=scalar
	def symb_forward(A,symb_input):return symb_input+A.scalar