import csv
class A:
	def __init__(A,instance,delimiter=';'):A.instance=instance;A.delimiter=delimiter
	def read(A):return csv.reader(A.instance.source,delimiter=A.delimiter)