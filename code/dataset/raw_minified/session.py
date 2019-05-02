'\nDeprecated and moved into tornado.handlers.base\n\n'
import warnings as A
A.warn('tinman.handlers.session moved to tinman.handlers.base',DeprecationWarning,stacklevel=2)
from tinman.handlers.base import SessionRequestHandler