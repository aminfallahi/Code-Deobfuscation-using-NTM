'Assertions related to networking.'
C=None
from hospital.utils.networking import ping
def A(host,timeout=1,msg=C):
	"Assert ``host`` responds to ping within ``timeout``.\n\n    >>> from hospital import assert_ping\n    >>> assert_ping('hospital.readthedocs.org')\n\n    ";B=timeout;A=msg
	if A is C:A='Failed to ping {host} within {timeout}.'.format(host=host,timeout=B)
	assert ping(host,B)is True,A