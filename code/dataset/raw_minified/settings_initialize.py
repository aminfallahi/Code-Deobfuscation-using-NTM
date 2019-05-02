'\nInitialize default values into DB.\n'
from django.core.management.base import BaseCommand as A
from django_settings.dataapi import initialize_data as B
class C(A):
	help='Initialize default values into DB';args=''
	def handle(A,**C):B()