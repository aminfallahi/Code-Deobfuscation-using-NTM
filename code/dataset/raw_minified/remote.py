from appvalidator.python.HTMLParser import HTMLParser as A
class B(A):
	def __init__(B,err):A.__init__(B);B.err=err
	def handle_starttag(B,tag,attrs):
		C='manifest';A=attrs
		if tag=='html':
			A=dict(A)
			if C in A:B.err.metadata['appcache']=A[C]