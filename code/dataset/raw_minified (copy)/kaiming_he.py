import os
from util import run
from deepy.utils import KaimingHeInitializer as A
B=os.path.join(os.path.dirname(__file__),'models','kaiming_he1.gz')
if __name__=='__main__':run(A(),B)