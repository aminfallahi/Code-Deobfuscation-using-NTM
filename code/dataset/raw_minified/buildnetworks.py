from django.core.management.base import BaseCommand as A,CommandError
from migrate_dns.network_build import migrate_networks as B
import pdb
class C(A):
	args='';help=''
	def handle(A,*C,**D):B()