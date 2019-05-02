from version import VERSION as B
class A:
	'\n    Set a X-Sikteeri-Version header to the response\n\n    The X-Sikteeri-Version header is intended to convey the deployed version\n    number of the project reliably.\n    '
	def process_response(C,request,response):A=response;A['X-Sikteeri-Version']=B;return A