'\nSupport for python 2 & 3, ripped pieces from six.py\n'
import sys
A=sys.version_info[0]==3
if A:B=str,
else:B=basestring,