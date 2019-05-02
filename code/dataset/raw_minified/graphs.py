'\nAccess layer for datasets used for testing graph kernels\n'
__author__='kasiajanocha'
import numpy as B
def A(size):A=B.random.random_integers(0,1,(size,size));A=(A+A.T)%2;B.fill_diagonal(A,1);return A