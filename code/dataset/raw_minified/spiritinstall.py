from __future__ import unicode_literals
from django.core.management.base import BaseCommand as A
from django.core.management import call_command as B
class C(A):
	help='Install Spirit.'
	def handle(A,*C,**D):B('migrate',stdout=A.stdout,stderr=A.stderr);B('createcachetable',stdout=A.stdout,stderr=A.stderr);B('collectstatic',stdout=A.stdout,stderr=A.stderr,verbosity=0);A.stdout.write('ok')