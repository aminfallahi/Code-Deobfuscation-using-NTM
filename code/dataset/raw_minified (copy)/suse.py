'\nOpen Suse OpenId backend, docs at:\n    http://psa.matiasaguirre.net/docs/backends/suse.html\n'
from social.backends.open_id import OpenIdAuth as A
class B(A):
	name='opensuse';URL='https://www.opensuse.org/openid/user/'
	def get_user_id(A,details,response):'\n        Return user unique id provided by service. For openSUSE\n        the nickname is original.\n        ';return details['nickname']