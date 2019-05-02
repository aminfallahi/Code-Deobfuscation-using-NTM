import os
from util import run
from deepy.utils import GaussianInitializer as A
B=os.path.join(os.path.dirname(__file__),'models','gaussian1.gz')
if __name__=='__main__':run(A(deviation=0.1),B)