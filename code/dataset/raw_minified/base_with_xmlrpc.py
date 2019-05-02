from pylons import tmpl_context as c,app_globals,cache,request,session
from pylons.controllers import WSGIController,XMLRPCController
from pylons.controllers.util import abort,etag_cache,redirect
from pylons.decorators import jsonify,validate
from pylons.templating import render_mako as render
from pylons.i18n import N_,_,ungettext
import projectname.model as model,projectname.lib.helpers as h
class BaseController(WSGIController):
	def __call__(self,environ,start_response):return WSGIController.__call__(self,environ,start_response)
__all__=[__name for __name in locals().keys()if not __name.startswith('_')or __name=='_']