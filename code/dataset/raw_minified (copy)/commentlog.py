from django.core.management.base import BaseCommand as A
from olympia.amo.utils import chunked as B
from olympia.devhub.models import ActivityLog as C
from olympia.editors.tasks import add_commentlog as D
class E(A):
	help='Add a CommentLog entry for all ActivityLog items'
	def handle(F,*G,**H):
		A=C.objects.review_queue().values_list('pk',flat=True).order_by('id')
		for E in B(A,100):D.delay(E)