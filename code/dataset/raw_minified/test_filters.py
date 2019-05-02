C='f'
from mahotas import _filters as A
from nose.tools import raises as B
@B(ValueError)
def D():A._check_mode('nayrest',0.0,C)
@B(NotImplementedError)
def E():A._check_mode('constant',1.2,C)
def F():
	for B in A.modes:A._check_mode(B,0.0,C)