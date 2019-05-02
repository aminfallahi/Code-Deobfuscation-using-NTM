from cleo.commands import Command as A
class B(A):
	def configure(A):A.set_name('foobar:foo').set_description('The foobar:foo command')
	def execute(A,input_,output_):A.input=input_;A.output=output_