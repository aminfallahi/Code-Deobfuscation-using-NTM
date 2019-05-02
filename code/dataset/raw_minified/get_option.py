from django import template as A
B=A.Library()
@B.filter
def C(server,command):
	try:A=server.config_options.get(command=command);return A.get_value()
	except:return''