D=print
from circuits import Component as A
class B(A):
	def started(A,*B):D("Hello I'm Bob!")
class C(A):
	def started(A,*B):D("Hello I'm Fred!")
(B()+C()).run()