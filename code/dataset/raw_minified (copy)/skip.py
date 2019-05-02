import pytest as A
B=True
@A.mark.parametrize('x',xrange(5000))
def C(x):
	if B:A.skip('heh')