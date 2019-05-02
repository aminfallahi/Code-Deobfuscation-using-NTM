'\nTinyURL.com shortener implementation\nNo config params needed\n'
from .base import BaseShortener as A
from ..exceptions import ShorteningErrorException as C
class B(A):
	api_url='http://tinyurl.com/api-create.php'
	def short(B,url):
		A=B._get(B.api_url,params=dict(url=url))
		if A.ok:return A.text
		raise C('There was an error shortening this url - {0}'.format(A.content))