from django.db import connection as A
from django.core.management.base import BaseCommand as B
from kitsune.manage import path
class C(B):
	help='Anonymize the database. Will wipe out some data.'
	def handle(E,*F,**G):
		with open(path('scripts/anonymize.sql'))as B:C=B.read();D=A.cursor();D.execute(C)