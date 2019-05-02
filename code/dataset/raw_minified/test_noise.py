import pytest as C
from keras.utils.test_utils import layer_test as A
from keras.layers import noise as B
def D():A(B.GaussianNoise,kwargs={'sigma':1.0},input_shape=(3,2,3))
def E():A(B.GaussianDropout,kwargs={'p':0.5},input_shape=(3,2,3))
if __name__=='__main__':C.main([__file__])