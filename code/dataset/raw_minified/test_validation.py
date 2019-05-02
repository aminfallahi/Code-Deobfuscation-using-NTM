'Tests for input validation functions.'
import numpy as A
from sklearn_theano.utils import check_tensor as B
from sklearn.utils.testing import assert_equal as C
from sklearn.utils.testing import assert_raises as E
def D():'Test that check_tensor works for a variety of inputs.';D=A.zeros((3,4,5));C(B([1,2]).shape,(2,));E(ValueError,B,D,dtype=A.float,n_dim=1);C(B(D,dtype=A.float,n_dim=6).shape,(1,1,1,3,4,5));C(B(D,dtype=A.float,n_dim=3).shape,(3,4,5))