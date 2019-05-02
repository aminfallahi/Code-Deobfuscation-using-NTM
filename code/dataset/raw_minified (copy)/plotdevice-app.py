import sys
from os.path import dirname as A,abspath as B,join
sys.path.append(join(A(B(__file__)),'python'))
import plotdevice.gui,AppKit as C
from signal import signal as D,SIGINT as E
D(E,lambda m,n:C.NSApplication.sharedApplication().terminate_(True))
from PyObjCTools import AppHelper as F
F.runEventLoop()