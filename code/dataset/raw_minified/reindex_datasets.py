from django.core.management.base import NoArgsCommand as B
from django.utils.translation import ugettext as A
from panda.models import Dataset as D
class C(B):
	help=A('Reindex all datasets')
	def handle_noargs(B,**E):
		for C in D.objects.all():C.update_full_text();B.stdout.write(A('Updated: %s\n')%C.name)
		B.stdout.write(A('Done!\n'))