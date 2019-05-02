import csv
class A:
	def __init__(A,file):
		B=file
		if isinstance(B,basestring):C=open(B,'rb')
		else:C=B
		A.reader=csv.DictReader(C);A.columns=[B.lower()for B in A.reader.fieldnames]
	def __iter__(A):
		for B in A.reader:(yield dict(((A.lower(),C)for(A,C)in B.items())))