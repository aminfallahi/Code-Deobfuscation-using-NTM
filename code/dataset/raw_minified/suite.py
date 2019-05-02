from unittest import TestSuite as A
class B(A):
	def run(C,result):
		B=result
		for D in C._tests:
			if B.shouldStop:break
			A=D(B)
			if A is not None and hasattr(A,'__iter__'):
				for E in A:(yield E)
		(yield)