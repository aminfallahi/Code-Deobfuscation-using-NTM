from django.core.management.base import BaseCommand as A
class B(A):
	' The update_index command exists in order to disable built-in haystack\n        command. '
	def handle(A,*B,**C):0