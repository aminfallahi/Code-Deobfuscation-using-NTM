from django.core.management.base import BaseCommand as A
from celery.task.sets import TaskSet as B
from olympia.amo.utils import chunked as C
from olympia.devhub.models import ActivityLog as D
from olympia.editors.tasks import add_versionlog as E
class F(A):
	help='Add a VersionLog entry for all ActivityLog items'
	def handle(G,*H,**I):A=D.objects.review_queue().values_list('pk',flat=True).order_by('id');F=[E.subtask(args=[B])for B in C(A,100)];B(F).apply_async()