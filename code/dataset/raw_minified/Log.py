from .Module import Module as A
import theano.tensor as B
class C(A):
	def symb_forward(A,symb_input):return B.log(symb_input)