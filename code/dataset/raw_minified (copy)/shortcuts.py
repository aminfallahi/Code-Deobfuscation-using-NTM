'\nsentry.utils.shortcuts\n~~~~~~~~~~~~~~~~~~~~~~\n\n:copyright: (c) 2010 by the Sentry Team, see AUTHORS for more details.\n:license: BSD, see LICENSE for more details.\n'
from flask import abort
def A(Model,**B):
	A=Model
	try:return A.objects.get(**B)
	except A.DoesNotExist:abort(404)