"Integrate eventlet with twisted's reactor mainloop.\n\nYou generally don't have to use it unless you need to call reactor.run()\nyourself.\n"
from eventlet.hubs.twistedr import BaseTwistedHub as B
from eventlet import use_hub as C
from eventlet.support import greenlets as D
from eventlet.hubs import _threadlocal as A
C(B)
assert not hasattr(A,'hub')
E=A.hub=A.Hub(D.getcurrent())