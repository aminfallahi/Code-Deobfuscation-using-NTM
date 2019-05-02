B=None
from django.contrib.auth.backends import ModelBackend as C
from django.contrib.auth.models import User as A
class D(C):
	def authenticate(C,decoded_data=B):
		try:return A.objects.get(id=decoded_data['user_id'])
		except A.DoesNotExist:return B
	def get_user(C,user_id):
		try:return A.objects.get(pk=user_id)
		except A.DoesNotExist:return B