import sys
from django.core.management.base import BaseCommand as A
from migrate_dns.import_utils import show_possible_imports as B
class C(A):
	args=''
	def handle(A,*C,**D):B(*sys.argv[2:])