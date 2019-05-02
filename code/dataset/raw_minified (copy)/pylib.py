from py.magic import greenlet as B
import sys,types
def A():C='greenlet';A=types.ModuleType(C);sys.modules[C]=A;A.greenlet=B;A.getcurrent=B.getcurrent;A.GreenletExit=B.GreenletExit