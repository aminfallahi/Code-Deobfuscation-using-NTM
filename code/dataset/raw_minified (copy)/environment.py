import random as B,theano as A,numpy as C
__all__='sandbox','reproducible'
def D():A.config.linker='py';A.config.mode='FAST_COMPILE';A.config.optimizer='fast_compile';A.config.allow_gc=False
def E(seed=0):C.random.seed(seed);B.seed(seed)