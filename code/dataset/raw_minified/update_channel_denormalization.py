from django.core.management.base import BaseCommand as A,CommandError
from opps.channels.models import Channel as B
from opps.containers.models import ContainerBox as C
from opps.articles.models import Post
class D(A):
	def handle(E,*F,**G):
		A=[B,Post,C]
		for D in A:[A.save()for A in D.objects.all()]