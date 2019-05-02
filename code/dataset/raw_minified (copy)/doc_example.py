from larch import Interpreter as C
from larch_plugins.xafs.autobk import autobk as D
from larch_plugins.io.xdi import read_xdi as E
B=C()
A=E('../xafsdata/fe3c_rt.xdi',_larch=B)
A.mu=A.mutrans
D(A,rbkg=1.0,kweight=2,_larch=B)