'Tests for compilation utilities.'
import os
from nose.tools import eq_,assert_raises as B
import pylearn2 as C
from pylearn2.utils.image import load as A
def D():'\n    Test utils.image.load\n    ';B(AssertionError,A,1);D=os.path.join(C.__path__[0],'utils','tests','example_image','mnist0.jpg');E=A(D);eq_(E.shape,(28,28,1))