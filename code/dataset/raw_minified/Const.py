import numpy as A
def B(value):
	B=value;C=A.array(B).dtype
	def D(shape,fan):return A.full(shape,B,dtype=C)
	return D
def C(value):
	def B(shape,fan):C=shape;B=A.array(value,copy=True);assert B.shape==C,'Shape mismatch in initializer: provided {}, requested {}'.format(B.shape,C);return B
	return B