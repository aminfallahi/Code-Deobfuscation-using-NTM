import numpy as A
def B(std):
	def B(shape,fan):return std*A.random.randn(*shape)
	return B