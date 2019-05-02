E='database'
from optparse import make_option as B
from django.core.management.base import NoArgsCommand as A
from django.db import DEFAULT_DB_ALIAS as C
from denorm import denorms as D
class F(A):
	option_list=A.option_list+(B('--database',action='store',dest=E,default=C,help='Nominates a database to execute SQL into. Defaults to the "default" database.'),);help='Creates all triggers needed by django-denorm.'
	def handle_noargs(C,**A):B=A[E];D.install_triggers(using=B)