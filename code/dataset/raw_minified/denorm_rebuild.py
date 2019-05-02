from django.core.management.base import BaseCommand as A
from denorm import denorms as B
class C(A):
	help='Recalculates the value of every single denormalized model field in the whole project.'
	def handle(D,model_name=None,*E,**A):C=int(A.get('verbosity',0));B.rebuildall(verbose=C>1,model_name=model_name)