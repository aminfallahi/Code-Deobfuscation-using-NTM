C=ImportError
def B():
	try:import workflow;return'Editorial'
	except C:
		try:import scene;return'Pythonista'
		except C:return None
A=B()
print('Yeah!!  '+A if A else'Sublime or other non-OMZ Software platform.')