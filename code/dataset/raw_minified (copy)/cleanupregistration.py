'\nA management command which deletes expired accounts (e.g.,\naccounts which signed up but never activated) from the database.\n\nCalls ``RegistrationProfile.objects.delete_expired_users()``, which\ncontains the actual logic for determining which accounts are deleted.\n\n'
from django.core.management.base import NoArgsCommand as A
from registration.models import RegistrationProfile as B
class C(A):
	help='Delete expired user registrations from the database'
	def handle_noargs(A,**C):B.objects.delete_expired_users()