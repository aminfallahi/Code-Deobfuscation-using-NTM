'module to test datasets.wiskott'
from pylearn2.datasets.wiskott import Wiskott as A
import unittest
from pylearn2.testing.skip import skip_if_no_data as B
from pylearn2.utils import isfinite as C
import numpy as D
def E():'loads wiskott dataset';B();D=A();assert C(D.X)