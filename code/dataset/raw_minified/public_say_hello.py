from flask.views import View
class A(View):
	def dispatch_request(A,username):return 'Hello {}'.format(username)