from __future__ import absolute_import,unicode_literals
from django.core.management.base import BaseCommand as A
from wagtail.wagtailsearch import models as B
class C(A):
	def handle(A,**D):C='Done';A.stdout.write('Cleaning daily hits records... ');B.QueryDailyHits.garbage_collect();A.stdout.write(C);A.stdout.write('Cleaning query records... ');B.Query.garbage_collect();A.stdout.write(C)