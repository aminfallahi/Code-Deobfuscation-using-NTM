import os
from dennis.cmdline import click_run as A
B=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def C(components):return os.path.join(B,*components)
if __name__=='__main__':A()