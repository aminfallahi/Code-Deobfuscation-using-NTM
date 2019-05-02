import os as A,sys
try:B=__file__
except NameError:B=sys.argv[0]
C=A.path.join(A.path.dirname(A.path.dirname(A.path.abspath(B))),'paste')
if A.path.exists(C):sys.path.insert(0,A.path.dirname(C))
from paste.script import command as D
D.run()