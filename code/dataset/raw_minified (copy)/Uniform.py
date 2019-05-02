import numpy as A
def B(low,high):
	def B(shape,fan):return A.random.uniform(low=low,high=high,size=shape)
	return B