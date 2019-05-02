'\nModule for running arbitrary tests with a __virtual__ function\n'
from __future__ import absolute_import
def __virtual__():return False,'The test_virtual execution module failed to load.'
def A():return True