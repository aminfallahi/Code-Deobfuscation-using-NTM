import DeepFried2 as A
from theano.tensor.nnet import relu
class B(A.Module):
	def __init__(B,alpha=0):A.Module.__init__(B);B.alpha=alpha
	def symb_forward(A,symb_input):return relu(symb_input,A.alpha)