from django.core.management.base import BaseCommand as A
from chronam.core.management.commands import configure_logging as B
from chronam.core.index import index_pages as C
B('index_pages_logging.config','index_pages.log')
class D(A):
	def handle(A,**B):C()