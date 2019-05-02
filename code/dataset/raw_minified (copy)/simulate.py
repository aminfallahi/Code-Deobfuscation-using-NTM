__author__='Ian Goodfellow'
from pylearn2.config import yaml_parse as A
import sys
D,B=sys.argv
C=A.load_path(B)
C.main_loop()