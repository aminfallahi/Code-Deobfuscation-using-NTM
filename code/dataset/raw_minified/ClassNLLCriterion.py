import theano.tensor as A
class B:
	def symb_forward(D,symb_input,symb_targets):B=symb_targets;C=A.cast(B,'int32');return A.mean(-A.log(symb_input[(A.arange(B.shape[0]),C)]))