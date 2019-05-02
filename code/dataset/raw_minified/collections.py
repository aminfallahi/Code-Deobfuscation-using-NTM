import sys
A=None
if sys.version_info>=(3,0):import collections as B;A=B.OrderedDict
else:import provision.ordered_dict;A=provision.ordered_dict.OrderedDict