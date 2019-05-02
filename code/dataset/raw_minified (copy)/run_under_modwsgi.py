from itty import *
@get('/')
def hello(request):return'Hello World!'
def application(environ,start_response):return handle_request(environ,start_response)