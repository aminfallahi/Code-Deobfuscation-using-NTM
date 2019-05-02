'\nUsage: print_model.py <pickle file containing a model>\nPrints out a saved model.\n'
from __future__ import print_function
__author__='Ian Goodfellow'
import sys
from pylearn2.utils import serial as A
if __name__=='__main__':D,B=sys.argv;C=A.load(B);print(C)