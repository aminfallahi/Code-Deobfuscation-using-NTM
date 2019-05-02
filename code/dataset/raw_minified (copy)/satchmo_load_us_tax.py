from django.core.management.base import NoArgsCommand as A
from django.core.management import call_command as B
class C(A):
	help='Load Satchmo country (l10n) data.'
	def handle_noargs(A,**C):'Load l10n fixtures';B('loaddata','us_tax.yaml',interactive=True)