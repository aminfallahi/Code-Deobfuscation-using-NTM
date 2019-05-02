from __future__ import unicode_literals
C=list
__author__='zeus'
from django.core.management.base import BaseCommand as A
from pybb.models import Topic,Post
from django.core import serializers as B
class D(A):
	args='<topic_id topic_id>';help='Dump target topics to json'
	def handle(D,*E,**H):A=[int(A)for A in E];F=C(Topic.objects.filter(id__in=A))+C(Post.objects.filter(topic_id__in=A));G=B.serialize('json',F);D.stdout.write(G)