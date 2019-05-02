'\nThis module holds controller components of\na typical glim app.\n'
class A:
	'\n    The controller component is responsible for handling requests\n    and returning appropriate response to the requests.\n\n    Attributes\n    ----------\n      request (bottle.request): Thread safe bottle request object\n      response (bottle.response): Thread safe bottle response object\n    '
	def __init__(A,request,response):A.request=request;A.response=response