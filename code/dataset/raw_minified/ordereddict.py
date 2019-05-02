from sys import version_info as A
if A>=(2,7):from collections import OrderedDict
else:from ._bundled.ordereddict import OrderedDict