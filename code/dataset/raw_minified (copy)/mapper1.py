import csv
from framework import Mapper as A
class B(A):
	def map(A):
		for B in A:A.emit(B[2],B[1])
	def read(A):
		B=csv.reader(A.infile)
		for C in B:(yield C)
if __name__=='__main__':C=B();C.map()