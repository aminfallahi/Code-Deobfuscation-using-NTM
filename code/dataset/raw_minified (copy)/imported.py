A=None
def B(arg1,kwarg1=A):'custom docstring';return'testfunc1: %s, %s'%(arg1,kwarg1)
class C:
	'wrong custom docstring'
	def testmeth1(A,arg1,kwarg1=A):'custom docstring';return'TestClass1.testmeth1: %s, %s'%(arg1,kwarg1)
class D:
	'wrong custom docstring'
	class Embed:
		'wrong custom docstring'
		def testmeth1(A,arg1,kwarg1=A):'custom docstring';return'TestClass12.Embed.testmeth1: %s, %s'%(arg1,kwarg1)