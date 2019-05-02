from circuits import Component as B
from circuits.web import Server as C,Logger as D,JSONRPC as E
class F(B):
	def foo(A,a,b,c):return a,b,c
A=C(('0.0.0.0',8000))
D().register(A)
E().register(A)
F().register(A)
A.run()