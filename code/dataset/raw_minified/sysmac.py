from __future__ import print_function
import pyeapi as A
A.load_config('nodes.conf')
B=A.connect_to('veos01')
C=B.enable('show version')
print(('My System MAC address is',C[0]['result']['systemMacAddress']))