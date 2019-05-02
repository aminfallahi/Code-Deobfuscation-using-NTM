from pylearn2.utils.bit_strings import all_bit_strings as B
import numpy as A
def C():A.testing.assert_equal((B(3)*2**A.arange(2,-1,-1)).sum(axis=1),A.arange(2**3))