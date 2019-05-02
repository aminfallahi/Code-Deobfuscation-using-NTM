E='checkindex'
from optparse import make_option as B
from django.core.management.base import BaseCommand as A
from kitsune.search.es_utils import es_status_cmd as C
from kitsune.search.utils import FakeLogger as D
class F(A):
	help='Shows elastic search index status.';option_list=A.option_list+(B('--checkindex',action='store_true',dest=E,help='Checks the index contents'),)
	def handle(A,*F,**B):C(B[E],log=D(A.stdout))