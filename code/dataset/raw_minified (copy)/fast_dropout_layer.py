from layer import *
from logistic_layer import *
from linear_layer import *
from softmax_layer import *
class FastDropoutLayer(Layer):0
class FastDropoutLogisticLayer(FastDropoutLayer,LogisticLayer):0
class FastDropoutLinearLayer(FastDropoutLayer,LinearLayer):0
class FastDropoutSoftmaxLayer(FastDropoutLayer,LinearLayer):0