from django.core.management.base import NoArgsCommand as A,CommandError
from django.utils.crypto import get_random_string as B
def C():A='abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)';return B(50,A)
class D(A):
	help='Generate a secret key for Django settings'
	def handle_noargs(A,**D):B=C();A.stdout.write("SECRET_KEY = '{}'".format(B))