E=Exception
class A(E):
	def __repr__(A):raise RuntimeError("I'm a bad class!")
def B():B=A();return B
def C():B=A();raise B
B()
try:C()
except E as D:print(D)