class A:
	def __init__(A):A.my_function()
	def my_function(A):raise A.not_implemented()
	def not_implemented(B):import inspect as A;C='Class {} does not implement {}()';D=A.getouterframes(A.currentframe(),2)[1][3];return NotImplementedError(C.format(B.__class__.__name__,D))
A()