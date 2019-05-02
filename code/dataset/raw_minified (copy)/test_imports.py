from circuits.core.components import BaseComponent as A
def B():
	try:from circuits.core.pollers import BasePoller as B;assert issubclass(B,A)
	except ImportError:assert False