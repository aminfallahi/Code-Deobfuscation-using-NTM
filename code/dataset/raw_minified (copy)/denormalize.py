from django.core.management.base import NoArgsCommand as A,CommandError as B
class C(A):
	def handle_noargs(A,**C):raise B('This management command is deprecated. Please consult the documentation for a command reference.')