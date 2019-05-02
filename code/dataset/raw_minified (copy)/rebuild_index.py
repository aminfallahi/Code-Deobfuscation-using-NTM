from django.core.management.base import BaseCommand as A
class B(A):
	' The rebuild_index command exists in order to disable built-in haystack\n        command. The django-sphinxdoc application uses this command under the\n        hood and out of control, what clears index at end of each deployment.\n    '
	def handle(A,*B,**C):0