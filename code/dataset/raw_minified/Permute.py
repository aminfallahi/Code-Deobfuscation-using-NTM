import DeepFried2 as A
class B(A.Module):
	def __init__(B,*C):A.Module.__init__(B);B.new_dims=C
	def symb_forward(A,symb_input):return symb_input.dimshuffle(*A.new_dims)