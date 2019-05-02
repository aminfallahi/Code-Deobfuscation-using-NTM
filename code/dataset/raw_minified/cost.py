from deepy.utils import CrossEntropyCost as B,EPSILON as C
import theano.tensor as A
class D(B):
	def get(D):B=A.clip(D.result_tensor,C,1.0-C);B=B.reshape((-1,B.shape[-1]));E=D.index_tensor.reshape((-1,));return-A.mean(A.log2(B[(A.arange(E.shape[0]),E)]))