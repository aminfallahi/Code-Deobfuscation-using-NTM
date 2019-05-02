D='poll'
import pytest as B
from rb import clients as C
from rb.poll import available_pollers as A
@B.mark.parametrize(D,A,ids=[B.__name__ for B in A])
def E(cluster,poll,monkeypatch):
	monkeypatch.setattr(C,D,poll);B=cluster.get_routing_client()
	with B.map()as E:
		for A in xrange(10):E.set('key:%s'%A,A)
	for A in xrange(10):assert B.get('key:%d'%A)==str(A)