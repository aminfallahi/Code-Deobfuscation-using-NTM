import numpy as A
def B(gain=1):
	def B(shape,fan):return gain*A.eye(*shape)
	return B