from django.core.management.base import BaseCommand as B
from freeze import scanner as C,settings as A,writer as D
class E(B):
	help='Generate static site.'
	def handle(B,**E):D.write(C.scan(),html_in_memory=A.FREEZE_ZIP_ALL,zip_all=A.FREEZE_ZIP_ALL,zip_in_memory=False);return