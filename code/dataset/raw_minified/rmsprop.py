import theano as F,theano.tensor as G,numpy as H
def A(params,gradients,momentum=0.9,learning_rate=0.01):
	'\n    RMSPROP optimization core.\n    ';C=momentum
	for (A,B) in zip(params,gradients):D=F.shared(H.zeros_like(A.get_value()),name=A.name+'_rms');E=C*D+(1-C)*B*B;(yield(D,E));(yield(A,A-learning_rate*B/G.sqrt(E+1e-08)))