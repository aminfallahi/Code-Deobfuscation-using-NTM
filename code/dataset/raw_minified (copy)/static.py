from pump.middleware.file import *
def wrap_static(app,public_dir,static_urls):
	app_with_file=wrap_file(app,public_dir)
	def wrapped_app(req):
		if any([req['uri'].startswith(s)for s in static_urls]):return app_with_file(req)
		else:return app(req)
	return wrapped_app