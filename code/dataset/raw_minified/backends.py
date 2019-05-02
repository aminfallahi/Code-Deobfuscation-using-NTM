from registration.backends.simple.views import RegistrationView as A
class B(A):
	def get_success_url(A,request,user):return'registration_create_thing'