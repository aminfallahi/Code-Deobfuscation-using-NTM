_A='message'
import toto
from toto.invocation import *
from toto.events import EventManager
@requires(_A)
def invoke(handler,params):EventManager.instance().send(_A,params[_A]);return'message sent!'