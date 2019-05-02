' Tests for skspec.core.Spectra class.  Much inspiration was taken from the pandas\namazing test suite, so thank you to the pandas team for such diligence.\n\nhttps://github.com/pydata/pandas/blob/master/pandas/tests/test_frame.py\n'
from copy import deepcopy
import sys,operator,nose
from numpy import random,nan
from numpy.random import randn
import numpy as A,numpy.ma as B
from numpy.testing import assert_array_equal
import numpy.ma.mrecords as C