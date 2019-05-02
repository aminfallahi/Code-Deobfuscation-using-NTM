import os
from util import run
from deepy.utils import UniformInitializer as A
B=os.path.join(os.path.dirname(__file__),'models','uniform1.gz')
if __name__=='__main__':run(A(),B)