import sys,os
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from pycoram.pycoram import PycoramIp as B
import ctrl_thread as C
A=B(topmodule='userlogic',if_type='axi',memimg='../../mem-incr.hex')
A.add_include_path('../../include/')
A.add_rtl('userlogic.v')
A.add_controlthread(C.ctrl_thread,threadname='ctrl_thread')
A.generate()