from pyramid.events import ApplicationCreated as A,subscriber as B
from .  import statsd_incr as C
@B(A)
def D(event):C('started')