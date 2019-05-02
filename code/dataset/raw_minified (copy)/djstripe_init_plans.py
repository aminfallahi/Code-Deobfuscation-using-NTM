from __future__ import unicode_literals
from django.core.management.base import BaseCommand as A
from ...sync import sync_plans as B
class C(A):
	help='Make sure your Stripe account has the plans'
	def handle(A,*C,**D):B()