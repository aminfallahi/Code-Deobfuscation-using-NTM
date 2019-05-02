_B='client_error'
_A='client_type'
import logging
from toto.invocation import *
@requires(_B,_A)
def invoke(handler,parameters):
	'A convenince method for writing browser errors\n  to Toto\'s server log. It works with the ``registerErrorHandler()`` method in ``toto.js``.\n\n  The "client_error" parameter should be set to the string to be written to Toto\'s log.\n  Currently, the "client_type" parameter must be set to "browser_js" for an event\n  to be written. Otherwise, this method has no effect.\n\n  Requires: ``client_error``, ``client_type``\n  ';A='logged'
	if parameters[_A]!='browser_js':return{A:False}
	logging.error(str(parameters[_B]));return{A:True}