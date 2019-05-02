class A(Exception):
	def __init__(B,message='',*C,**D):super(A,B).__init__(*C,**D);B.message=message
class B(A):0
class C(A):0
class D(A):0