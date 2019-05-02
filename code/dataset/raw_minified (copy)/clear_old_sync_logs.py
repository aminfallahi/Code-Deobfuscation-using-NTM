from datetime import timedelta as A
from django.conf import settings as B
from django.core.management.base import BaseCommand as C
from django.utils import timezone as D
from pontoon.sync.models import SyncLog as E
class F(C):
	help='Delete sync logs that are older than settings.SYNC_LOG_RETENTION'
	def handle(F,*G,**H):C=D.now()-A(days=B.SYNC_LOG_RETENTION);E.objects.filter(start_time__lte=C).delete()