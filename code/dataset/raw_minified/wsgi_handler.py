import sys,os
A=os.path.dirname(os.path.abspath(__file__))
if A not in sys.path:sys.path.insert(0,A)
from uliweb.manage import make_simple_application as B
C=B(project_dir=A)