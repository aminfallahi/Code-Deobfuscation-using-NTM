from metakernel.tests.utils import get_kernel as C,get_log_text as D,clear_log_text,EvalKernel as E
import re,os
from metakernel.config import get_local_magics_dir as B
A=B()+os.sep+'cd_magic.py'
def F():B=C(E);B.do_execute('%install_magic https://raw.githubusercontent.com/calysto/metakernel/master/metakernel/magics/cd_magic.py');F=D(B);assert re.match(".*Downloaded '.*ipython/metakernel/magics/cd_magic.py'",F,re.DOTALL|re.M),'Not downloaded';assert os.path.isfile(A),'File not found: %s'%A
def G():os.remove(A)