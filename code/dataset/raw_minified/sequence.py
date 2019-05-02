from googkit.commands.command import Command as A
class B(A):
	'Command class that runs internal commands sequentially.'
	@classmethod
	def _internal_commands(A):return[]
	def run(A):
		for B in A.__class__._internal_commands():C=B(A.env);C.run()