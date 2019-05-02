import logging as A
from django.core.management.base import BaseCommand as B
from django.conf import settings as C
from chronam.core.essay_loader import load_essays as D
from chronam.core.management.commands import configure_logging as E
E('load_essays.config','load_essays.log')
F=A.getLogger()
class G(B):
	help='load all the essays'
	def handle(A,*B,**E):D(C.ESSAYS_FEED,index=True)