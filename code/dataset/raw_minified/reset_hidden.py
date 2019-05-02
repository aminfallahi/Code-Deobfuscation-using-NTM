from django.core.management.base import BaseCommand as A
from packages.models import Release as B,ReleaseFile as C
class D(A):
	def handle(E,*F,**G):D=False;A=True;B.objects.filter(hidden=A).update(hidden=D);C.objects.filter(hidden=A).update(hidden=D)