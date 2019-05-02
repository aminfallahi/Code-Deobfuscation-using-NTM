from django.core.management.base import BaseCommand as B
from django.conf import settings as A
from angular_scaffold.management.commands.helpers._generate_docs import generate_docs as C
class D(B):
	help='Adds a docs folder and some basic documentation'
	def handle(D,*E,**F):
		D.stdout.write('Generating documentation')
		if hasattr(A,'BASE_DIR'):B=A.BASE_DIR
		else:B='.'
		C(B)