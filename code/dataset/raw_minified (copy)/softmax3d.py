from layer import NeuralLayer as A
import theano,theano.tensor as B
class C(A):
	def __init__(A):super(C,A).__init__('softmax')
	def compute_tensor(D,x):A=x.shape;x=x.reshape((-1,A[-1]));C=B.nnet.softmax(x);return C.reshape(A)