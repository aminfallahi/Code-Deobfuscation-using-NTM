'\nApp Engine config\n\n'
def A():'Uncomment the first two lines to enable GAE Mini Profiler on production for admin accounts';return False
def B(app):A=app;from google.appengine.ext.appstats import recording as B;A=B.appstats_wsgi_middleware(A);return A