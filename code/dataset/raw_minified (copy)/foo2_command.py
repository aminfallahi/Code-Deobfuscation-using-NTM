from cleo.commands import Command as A
class B(A):
	def configure(A):A.set_name('foo1:bar').set_description('The foo1:bar command').set_aliases(['afoobar2'])
	def execute(A,input_,output_):0