import DeepFried2 as A
class B(A.Container):
	def __init__(B,axis=1):A.Container.__init__(B);B.axis=axis
	def symb_forward(B,symb_inputs):C=symb_inputs;assert isinstance(C,(list,tuple)),'Input to `{}` container needs to be a tuple or a list.'.format(A.utils.typename(B));return A.T.concatenate(C,B.axis)