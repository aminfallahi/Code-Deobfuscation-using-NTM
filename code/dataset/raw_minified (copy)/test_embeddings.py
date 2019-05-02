import pytest as A
from keras.utils.test_utils import layer_test as B
from keras.layers.embeddings import Embedding as C
import keras.backend as D
def E():B(C,kwargs={'output_dim':4.0,'input_dim':10,'input_length':2},input_shape=(3,2),input_dtype='int32',expected_output_dtype=D.floatx())
if __name__=='__main__':A.main([__file__])